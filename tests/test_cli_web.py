"""Tests for the CLI web subcommand."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from src.cli import main


class TestCLIWebCommand(unittest.TestCase):
    """CLI coverage for the browser entry point."""

    def test_web_subcommand_dispatches_to_start_web(self) -> None:
        with patch.object(sys, "argv", ["clawd", "web", "--host", "0.0.0.0", "--port", "9091"]):
            with patch("src.cli.start_web", return_value=0) as mock_start_web:
                result = main()

        self.assertEqual(result, 0)
        mock_start_web.assert_called_once_with(host="0.0.0.0", port=9091)

    def test_start_web_forwards_workspace_root(self) -> None:
        with patch("src.web.run_web_server") as mock_run_web:
            from src.cli import start_web

            with patch("src.cli.Path.cwd", return_value=Path("/tmp/clawd-web")):
                result = start_web(host="127.0.0.1", port=8080)

        self.assertEqual(result, 0)
        mock_run_web.assert_called_once_with(
            host="127.0.0.1",
            port=8080,
            workspace_root=Path("/tmp/clawd-web"),
        )
