"""Persistence for browser-specific session preferences."""

from __future__ import annotations

import json
import re
import threading
from pathlib import Path
from typing import Any


SESSION_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,120}$")


class WebSessionStore:
    """Keep web preferences separate from provider conversation persistence."""

    def __init__(self, home: Path | None = None) -> None:
        root = Path(home or Path.home()).resolve() / ".clawd"
        self.session_root = root / "sessions"
        self.preferences_root = root / "web_sessions"
        self._lock = threading.RLock()

    def list_session_ids(self) -> list[str]:
        if not self.session_root.exists():
            return []
        return sorted(
            path.stem
            for path in self.session_root.glob("*.json")
            if SESSION_ID_RE.fullmatch(path.stem)
        )

    def session_exists(self, session_id: str) -> bool:
        return self._session_path(session_id).is_file()

    def load_preferences(self, session_id: str) -> dict[str, Any]:
        path = self._preferences_path(session_id)
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        return value if isinstance(value, dict) else {}

    def save_preferences(self, session_id: str, value: dict[str, Any]) -> None:
        path = self._preferences_path(session_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        with self._lock:
            temp = path.with_suffix(f".{threading.get_ident()}.tmp")
            temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
            temp.replace(path)

    def delete(self, session_id: str) -> bool:
        deleted = False
        with self._lock:
            for path in (self._session_path(session_id), self._preferences_path(session_id)):
                try:
                    path.unlink()
                    deleted = True
                except FileNotFoundError:
                    continue
        return deleted

    def _session_path(self, session_id: str) -> Path:
        return self.session_root / f"{self._validate_id(session_id)}.json"

    def _preferences_path(self, session_id: str) -> Path:
        return self.preferences_root / f"{self._validate_id(session_id)}.json"

    @staticmethod
    def _validate_id(session_id: str) -> str:
        normalized = str(session_id or "").strip()
        if not SESSION_ID_RE.fullmatch(normalized):
            raise ValueError("invalid web session id")
        return normalized
