"""Safe packaging and lookup for browser-downloadable aircraft artifacts."""

from __future__ import annotations

import json
import re
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote
from uuid import uuid4


AIRCRAFT_RESULT_FILE_EXTENSIONS = {
    ".csv",
    ".docx",
    ".glb",
    ".gltf",
    ".html",
    ".json",
    ".log",
    ".md",
    ".obj",
    ".pdf",
    ".png",
    ".stl",
    ".svg",
    ".txt",
    ".vsp3",
    ".vspscript",
    ".xlsx",
}
AIRCRAFT_RESULT_EXCLUDED_FILENAMES = {".DS_Store", "SKILL.md"}
ARTIFACT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,120}$")
RESULT_FILE_CONTENT_TYPES = {
    ".csv": "text/csv; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".log": "text/plain; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".obj": "text/plain; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".txt": "text/plain; charset=utf-8",
    ".vspscript": "text/plain; charset=utf-8",
}
RESULT_FILE_KINDS = {
    ".csv": "data",
    ".html": "html",
    ".json": "json",
    ".log": "log",
    ".md": "markdown",
    ".obj": "model",
    ".png": "image",
    ".svg": "image",
    ".txt": "text",
    ".vspscript": "script",
}
PREVIEWABLE_RESULT_EXTENSIONS = set(RESULT_FILE_CONTENT_TYPES)


class AircraftArtifactStore:
    """Own artifact filtering, packaging, metadata, and safe download lookup."""

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = Path(workspace_root).resolve()
        self.root = self.workspace_root / ".clawd" / "generated" / "web_artifacts"

    def resolve_download(self, artifact_id: str) -> dict[str, Any]:
        normalized = unquote(artifact_id or "").strip()
        if not ARTIFACT_ID_RE.fullmatch(normalized):
            raise KeyError(f"Unknown artifact: {artifact_id}")

        root = self.root.resolve()
        matches = sorted(root.glob(f"*/{normalized}.zip"), key=lambda item: item.stat().st_mtime)
        if not matches:
            raise KeyError(f"Unknown artifact: {artifact_id}")

        path = matches[-1].resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise KeyError(f"Unknown artifact: {artifact_id}") from exc

        metadata: dict[str, Any] = {}
        metadata_path = path.with_suffix(".json")
        if metadata_path.exists():
            try:
                loaded = json.loads(metadata_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    metadata = loaded
            except (OSError, json.JSONDecodeError):
                metadata = {}

        return {
            "path": path,
            "filename": metadata.get("filename") or path.name,
            "content_type": "application/zip",
            "size_bytes": path.stat().st_size,
        }

    def package(self, owner_id: str, source_dir: Path) -> dict[str, Any] | None:
        source_dir = source_dir.resolve()
        try:
            source_dir.relative_to(self.workspace_root)
        except ValueError as exc:
            raise ValueError("artifact source directory is outside the workspace") from exc
        if not source_dir.is_dir():
            raise ValueError("artifact source directory does not exist")

        artifact_id = uuid4().hex
        created_at = datetime.now().isoformat(timespec="seconds")
        artifact_dir = self.root / owner_id
        artifact_dir.mkdir(parents=True, exist_ok=True)
        zip_path = artifact_dir / f"{artifact_id}.zip"
        source_rel = source_dir.relative_to(self.workspace_root).as_posix()
        filename = f"aircraft-design-result-{owner_id}-{artifact_id[:8]}.zip"

        included_files: list[Path] = []
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for file_path in sorted(source_dir.rglob("*")):
                if not file_path.is_file() or not self.should_include(file_path, source_dir):
                    continue
                arcname = Path(source_dir.name) / file_path.relative_to(source_dir)
                archive.write(file_path, arcname.as_posix())
                included_files.append(file_path)

            manifest = {
                "skill": "aircraft-design-skill",
                "display_name": "飞行器总体设计",
                "source_dir": source_rel,
                "packaged_at": created_at,
                "file_count": len(included_files),
                "files": [file.relative_to(source_dir).as_posix() for file in included_files],
            }
            archive.writestr(
                f"{source_dir.name}/download_manifest.json",
                json.dumps(manifest, ensure_ascii=False, indent=2),
            )

        if not included_files:
            zip_path.unlink(missing_ok=True)
            return None

        artifact = {
            "id": artifact_id,
            "kind": "aircraft_design_result_zip",
            "name": "飞行器总体设计结果包",
            "filename": filename,
            "format": "zip",
            "download_url": f"/api/artifacts/{artifact_id}/download",
            "size_bytes": zip_path.stat().st_size,
            "file_count": len(included_files),
            "source_dir": source_rel,
            "created_at": created_at,
            "summary": f"包含 {len(included_files)} 个设计产物，来源：{source_rel}",
        }
        zip_path.with_suffix(".json").write_text(
            json.dumps(artifact, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return artifact

    def list_result_files(self, owner_id: str, source_dir: Path) -> list[dict[str, Any]]:
        """List safe, browser-previewable files from one deterministic design run."""
        source_dir = self._validated_source_dir(source_dir)
        files: list[dict[str, Any]] = []
        for path in sorted(source_dir.rglob("*")):
            suffix = path.suffix.lower()
            if (
                not path.is_file()
                or not self.should_include(path, source_dir)
                or suffix not in PREVIEWABLE_RESULT_EXTENSIONS
            ):
                continue
            try:
                path.resolve().relative_to(source_dir)
            except ValueError:
                continue
            relative = path.relative_to(source_dir).as_posix()
            encoded_owner = quote(owner_id, safe="")
            encoded_path = quote(relative, safe="/")
            file_url = f"/api/design-jobs/{encoded_owner}/files/{encoded_path}"
            files.append(
                {
                    "name": path.name,
                    "path": relative,
                    "kind": RESULT_FILE_KINDS.get(suffix, "file"),
                    "format": suffix.lstrip("."),
                    "size_bytes": path.stat().st_size,
                    "preview_url": file_url,
                    "download_url": file_url + "?download=1",
                }
            )
        return files

    def resolve_result_file(self, source_dir: Path, relative_path: str) -> dict[str, Any]:
        """Resolve a run-relative result path without allowing workspace traversal."""
        source_dir = self._validated_source_dir(source_dir)
        normalized = unquote(relative_path or "").strip()
        relative = Path(normalized)
        if not normalized or relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
            raise KeyError(f"Unknown result file: {relative_path}")
        path = (source_dir / relative).resolve()
        try:
            path.relative_to(source_dir)
        except ValueError as exc:
            raise KeyError(f"Unknown result file: {relative_path}") from exc
        suffix = path.suffix.lower()
        if (
            not path.is_file()
            or not self.should_include(path, source_dir)
            or suffix not in PREVIEWABLE_RESULT_EXTENSIONS
        ):
            raise KeyError(f"Unknown result file: {relative_path}")
        return {
            "path": path,
            "filename": path.name,
            "content_type": RESULT_FILE_CONTENT_TYPES[suffix],
            "kind": RESULT_FILE_KINDS.get(suffix, "file"),
            "size_bytes": path.stat().st_size,
        }

    def file_count(self, source_dir: Path, *, direct: bool = False) -> int:
        if not source_dir.exists() or not source_dir.is_dir():
            return 0
        paths = source_dir.iterdir() if direct else source_dir.rglob("*")
        return sum(
            1
            for path in paths
            if path.is_file() and self.should_include(path, source_dir)
        )

    def fingerprint(self, source_dir: Path) -> tuple[int, int, int]:
        latest_ns = 0
        total_size = 0
        count = 0
        for path in source_dir.rglob("*"):
            if not path.is_file() or not self.should_include(path, source_dir):
                continue
            stat = path.stat()
            latest_ns = max(latest_ns, stat.st_mtime_ns)
            total_size += stat.st_size
            count += 1
        return latest_ns, total_size, count

    def latest_mtime(self, source_dir: Path) -> float:
        latest = source_dir.stat().st_mtime
        for path in source_dir.rglob("*"):
            if path.is_file() and self.should_include(path, source_dir):
                latest = max(latest, path.stat().st_mtime)
        return latest

    def _validated_source_dir(self, source_dir: Path) -> Path:
        source_dir = Path(source_dir).resolve()
        try:
            source_dir.relative_to(self.workspace_root)
        except ValueError as exc:
            raise ValueError("artifact source directory is outside the workspace") from exc
        if not source_dir.is_dir():
            raise ValueError("artifact source directory does not exist")
        return source_dir

    @staticmethod
    def should_include(path: Path, source_dir: Path) -> bool:
        source_dir = source_dir.resolve()
        try:
            relative = path.resolve().relative_to(source_dir)
        except ValueError:
            return False
        if any(part.startswith(".") for part in relative.parts):
            return False
        if path.name in AIRCRAFT_RESULT_EXCLUDED_FILENAMES:
            return False
        return path.suffix.lower() in AIRCRAFT_RESULT_FILE_EXTENSIONS
