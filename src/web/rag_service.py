"""In-process RAG index service for the browser UI."""

from __future__ import annotations

import copy
import importlib.util
import sqlite3
import sys
import threading
import time
from collections import OrderedDict
from pathlib import Path
from types import ModuleType
from typing import Any


class RagIndexService:
    """Reuse the local RAG search module without spawning a Python subprocess."""

    def __init__(self, workspace_root: Path, script_path: Path) -> None:
        self.workspace_root = Path(workspace_root).resolve()
        self.script_path = Path(script_path).resolve()
        self.data_dir = self.workspace_root / "RAG-data"
        self._module: ModuleType | None = None
        self._lock = threading.RLock()
        self._index_lock = threading.RLock()
        self._query_cache: OrderedDict[tuple[Any, ...], dict[str, Any]] = OrderedDict()
        self._query_cache_limit = 32
        self._rebuild_thread: threading.Thread | None = None
        self._rebuild_state: dict[str, Any] = {
            "running": False,
            "started_at": None,
            "finished_at": None,
            "error": None,
            "timings": {},
            "cache_path": None,
            "markdown_files": 0,
            "chunk_count": 0,
        }

    def search(self, query: str, settings: Any) -> dict[str, Any]:
        """Return the same JSON payload as the CLI retriever."""
        cleaned = query.strip()
        if not cleaned:
            raise ValueError("query must not be empty")

        module = self._load_module()
        values = self._settings_values(module, settings)
        top_k = values["top_k"]
        max_snippet_chars = values["max_snippet_chars"]
        use_cache = values["use_cache"]
        candidate_limit = values["candidate_limit"]
        cache_key = (cleaned, top_k, max_snippet_chars, use_cache, candidate_limit)

        with self._lock:
            cached = self._query_cache.get(cache_key)
            if cached is not None:
                self._query_cache.move_to_end(cache_key)
                payload = copy.deepcopy(cached)
                payload.setdefault("cache", {})["query_cache_hit"] = True
                return payload

        started_at = time.perf_counter()
        timings: dict[str, float] = {}
        data_dir = module.resolve_data_dir(self.data_dir)
        if data_dir is None:
            raise ValueError(f"data directory not found: {self.data_dir}")

        file_started = time.perf_counter()
        files = sorted(data_dir.rglob("*.md"))
        timings["file_scan_ms"] = _elapsed_ms(file_started)

        if not files:
            payload = {
                "query": cleaned,
                "data_dir": str(data_dir),
                "markdown_files_scanned": 0,
                "chunks_indexed": 0,
                "candidate_chunks": 0,
                "cache": {"enabled": use_cache, "hit": False, "path": None, "type": "sqlite"},
                "timings": _finish_timings(timings, started_at),
                "hits": [],
            }
        elif use_cache:
            with self._index_lock:
                hits, chunks_indexed, cache_info, candidate_count = module.search_with_sqlite_cache(
                    files=files,
                    data_dir=data_dir,
                    query=cleaned,
                    chunk_lines=values["chunk_lines"],
                    overlap_lines=values["overlap_lines"],
                    candidate_limit=max(candidate_limit, top_k),
                    cache_dir=None,
                    timings=timings,
                )
            payload = module.build_json_response(
                query=cleaned,
                data_dir=data_dir,
                files=files,
                chunks_indexed=chunks_indexed,
                hits=hits[: max(top_k, 1)],
                max_snippet_chars=max_snippet_chars,
                cache_info=cache_info,
                timings=_finish_timings(timings, started_at),
                candidate_count=candidate_count,
            )
        else:
            build_started = time.perf_counter()
            chunks, document_frequency, avg_length = module.build_index(
                files,
                chunk_lines=values["chunk_lines"],
                overlap_lines=values["overlap_lines"],
            )
            timings["index_build_ms"] = _elapsed_ms(build_started)
            search_started = time.perf_counter()
            hits = module.search_chunks(
                chunks,
                cleaned,
                document_frequency=document_frequency,
                avg_length=avg_length,
            )
            timings["search_ms"] = _elapsed_ms(search_started)
            payload = module.build_json_response(
                query=cleaned,
                data_dir=data_dir,
                files=files,
                chunks_indexed=len(chunks),
                hits=hits[: max(top_k, 1)],
                max_snippet_chars=max_snippet_chars,
                cache_info={"enabled": False, "hit": False, "path": None, "type": "memory"},
                timings=_finish_timings(timings, started_at),
                candidate_count=len(chunks),
            )

        with self._lock:
            self._query_cache[cache_key] = copy.deepcopy(payload)
            self._query_cache.move_to_end(cache_key)
            while len(self._query_cache) > self._query_cache_limit:
                self._query_cache.popitem(last=False)
        return payload

    def status(self, settings: Any | None = None) -> dict[str, Any]:
        """Return cache readiness and background rebuild state."""
        module = self._load_module()
        values = self._settings_values(module, settings)
        data_dir = module.resolve_data_dir(self.data_dir)
        resolved_data_dir = data_dir or self.data_dir.resolve()
        cache_path = module.get_cache_path(
            data_dir=resolved_data_dir,
            chunk_lines=values["chunk_lines"],
            overlap_lines=values["overlap_lines"],
            cache_dir=None,
        )
        files = sorted(data_dir.rglob("*.md")) if data_dir is not None else []
        cache_meta = self._read_cache_meta(cache_path)
        cache_exists = cache_path.exists()
        cache_ready = False
        manifest_ms = 0.0
        validate_ms = 0.0
        if data_dir is not None and files and cache_exists:
            manifest_started = time.perf_counter()
            manifest = module.build_file_manifest(files, data_dir)
            expected_manifest_hash = module.manifest_hash(manifest)
            manifest_ms = _elapsed_ms(manifest_started)
            validate_started = time.perf_counter()
            cache_ready = module.sqlite_cache_is_valid(
                cache_path,
                data_dir=data_dir,
                chunk_lines=values["chunk_lines"],
                overlap_lines=values["overlap_lines"],
                expected_manifest_hash=expected_manifest_hash,
            )
            validate_ms = _elapsed_ms(validate_started)

        with self._lock:
            rebuild = copy.deepcopy(self._rebuild_state)
            query_cache_size = len(self._query_cache)

        return {
            "available": self.script_path.exists(),
            "data_dir": str(resolved_data_dir),
            "markdown_files": len(files),
            "cache_path": str(cache_path),
            "cache_exists": cache_exists,
            "cache_ready": cache_ready,
            "cache_stale": cache_exists and not cache_ready,
            "cache": {
                "type": "sqlite",
                "path": str(cache_path),
                "exists": cache_exists,
                "ready": cache_ready,
                "stale": cache_exists and not cache_ready,
                "chunk_count": int(cache_meta.get("chunk_count", "0") or 0),
                "schema_version": cache_meta.get("schema_version"),
            },
            "settings": {
                "chunk_lines": values["chunk_lines"],
                "overlap_lines": values["overlap_lines"],
                "candidate_limit": values["candidate_limit"],
            },
            "timings": {
                "manifest_ms": manifest_ms,
                "cache_validate_ms": validate_ms,
            },
            "query_cache_size": query_cache_size,
            "rebuild": rebuild,
        }

    def rebuild(self, settings: Any | None = None, *, force: bool = True) -> dict[str, Any]:
        """Start a background SQLite index rebuild and return current status."""
        module = self._load_module()
        values = self._settings_values(module, settings)
        with self._lock:
            if self._rebuild_state.get("running"):
                return self.status(settings)
            self._rebuild_state = {
                "running": True,
                "started_at": time.time(),
                "finished_at": None,
                "error": None,
                "timings": {},
                "cache_path": None,
                "markdown_files": 0,
                "chunk_count": 0,
                "force": force,
            }
            thread = threading.Thread(
                target=self._rebuild_worker,
                args=(values, force),
                name="clawd-rag-index-rebuild",
                daemon=True,
            )
            self._rebuild_thread = thread
            thread.start()
        return self.status(settings)

    def cache_ready(self, settings: Any | None = None) -> bool:
        """Fast public helper for callers that need to avoid cold-path blocking."""
        return bool(self.status(settings).get("cache_ready"))

    def not_ready_payload(self, query: str, settings: Any | None = None) -> dict[str, Any]:
        """Return a JSON-shaped RAG payload when the cache is warming in the background."""
        module = self._load_module()
        values = self._settings_values(module, settings)
        status = self.status(settings)
        rebuild = status.get("rebuild") or {}
        message = (
            "RAG 索引正在后台构建；状态变为就绪后请重试。"
            if rebuild.get("running")
            else "RAG 索引尚未就绪；请先构建索引再运行检索。"
        )
        return {
            "query": query.strip(),
            "data_dir": status.get("data_dir") or str(self.data_dir),
            "markdown_files_scanned": status.get("markdown_files", 0),
            "chunks_indexed": (status.get("cache") or {}).get("chunk_count", 0),
            "candidate_chunks": 0,
            "cache": {
                "enabled": values["use_cache"],
                "hit": False,
                "path": status.get("cache_path"),
                "type": "sqlite",
                "candidate_limit": values["candidate_limit"],
                "ready": False,
                "build_in_progress": bool(rebuild.get("running")),
                "stale": bool(status.get("cache_stale")),
            },
            "timings": status.get("timings") or {},
            "message": message,
            "hits": [],
        }

    def _load_module(self) -> ModuleType:
        with self._lock:
            if self._module is not None:
                return self._module
            if not self.script_path.exists():
                raise ValueError(f"RAG search script not found: {self.script_path}")
            spec = importlib.util.spec_from_file_location("clawd_aircraft_design_rag_search", self.script_path)
            if spec is None or spec.loader is None:
                raise ValueError(f"Unable to load RAG search script: {self.script_path}")
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            try:
                spec.loader.exec_module(module)
            except Exception:
                sys.modules.pop(spec.name, None)
                raise
            self._module = module
            return module

    def _settings_values(self, module: ModuleType, settings: Any | None) -> dict[str, Any]:
        return {
            "top_k": int(getattr(settings, "top_k", 5)),
            "max_snippet_chars": int(getattr(settings, "max_snippet_chars", 280)),
            "use_cache": bool(getattr(settings, "use_cache", True)),
            "candidate_limit": int(
                getattr(settings, "candidate_limit", getattr(module, "DEFAULT_CANDIDATE_LIMIT", 1200))
            ),
            "chunk_lines": int(getattr(module, "DEFAULT_CHUNK_LINES", 120)),
            "overlap_lines": int(getattr(module, "DEFAULT_OVERLAP_LINES", 20)),
        }

    def _rebuild_worker(self, values: dict[str, Any], force: bool) -> None:
        module = self._load_module()
        started_at = time.perf_counter()
        timings: dict[str, float] = {}
        cache_path: Path | None = None
        markdown_files = 0
        chunk_count = 0
        error: str | None = None
        try:
            data_dir = module.resolve_data_dir(self.data_dir)
            if data_dir is None:
                raise ValueError(f"data directory not found: {self.data_dir}")

            file_started = time.perf_counter()
            files = sorted(data_dir.rglob("*.md"))
            markdown_files = len(files)
            timings["file_scan_ms"] = _elapsed_ms(file_started)
            if not files:
                raise ValueError(f"No Markdown files found under: {data_dir}")

            manifest_started = time.perf_counter()
            manifest = module.build_file_manifest(files, data_dir)
            expected_manifest_hash = module.manifest_hash(manifest)
            timings["manifest_ms"] = _elapsed_ms(manifest_started)
            cache_path = module.get_cache_path(
                data_dir=data_dir,
                chunk_lines=values["chunk_lines"],
                overlap_lines=values["overlap_lines"],
                cache_dir=None,
            )
            should_build = force or not module.sqlite_cache_is_valid(
                cache_path,
                data_dir=data_dir,
                chunk_lines=values["chunk_lines"],
                overlap_lines=values["overlap_lines"],
                expected_manifest_hash=expected_manifest_hash,
            )
            if should_build:
                build_started = time.perf_counter()
                with self._index_lock:
                    module.build_sqlite_index(
                        cache_path,
                        files=files,
                        data_dir=data_dir,
                        manifest=manifest,
                        expected_manifest_hash=expected_manifest_hash,
                        chunk_lines=values["chunk_lines"],
                        overlap_lines=values["overlap_lines"],
                    )
                timings["index_build_ms"] = _elapsed_ms(build_started)
            else:
                timings["index_build_ms"] = 0.0

            meta = self._read_cache_meta(cache_path)
            chunk_count = int(meta.get("chunk_count", "0") or 0)
            timings["total_ms"] = _elapsed_ms(started_at)
        except Exception as exc:  # pragma: no cover - defensive background path
            error = str(exc)
            timings["total_ms"] = _elapsed_ms(started_at)

        with self._lock:
            self._query_cache.clear()
            self._rebuild_state = {
                "running": False,
                "started_at": self._rebuild_state.get("started_at"),
                "finished_at": time.time(),
                "error": error,
                "timings": timings,
                "cache_path": str(cache_path) if cache_path is not None else None,
                "markdown_files": markdown_files,
                "chunk_count": chunk_count,
                "force": force,
            }

    def _read_cache_meta(self, cache_path: Path) -> dict[str, str]:
        if not cache_path.exists():
            return {}
        try:
            with sqlite3.connect(cache_path) as conn:
                return {str(row[0]): str(row[1]) for row in conn.execute("SELECT key, value FROM meta")}
        except Exception:
            return {}


def _elapsed_ms(started_at: float) -> float:
    return round((time.perf_counter() - started_at) * 1000, 3)


def _finish_timings(timings: dict[str, float], started_at: float) -> dict[str, float]:
    finished = dict(timings)
    finished["total_ms"] = _elapsed_ms(started_at)
    return finished
