from __future__ import annotations

import subprocess
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".clawd" / "skills" / "aircraft-design-rag" / "scripts" / "search_rag.py"

spec = spec_from_file_location("search_rag", SCRIPT)
assert spec is not None
search_rag = module_from_spec(spec)
assert spec.loader is not None
sys.modules["search_rag"] = search_rag
spec.loader.exec_module(search_rag)


def test_search_rag_finds_relevant_markdown_chunk(tmp_path: Path) -> None:
    data_dir = tmp_path / "RAG-data"
    data_dir.mkdir()

    (data_dir / "engines.md").write_text(
        "\n".join(
            [
                "# 发动机资料",
                "YF-21 液体火箭发动机用于运载火箭推进系统。",
                "它采用四台主发动机并联的设计方案。",
                "推力室与涡轮泵系统构成主要推进回路。",
            ]
        ),
        encoding="utf-8",
    )
    (data_dir / "airframes.md").write_text(
        "\n".join(
            [
                "# 机体设计",
                "机翼布局与气动外形决定升阻特性。",
                "复合材料机身可以降低结构重量。",
            ]
        ),
        encoding="utf-8",
    )

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--data-dir",
            str(data_dir),
            "--query",
            "YF-21 液体火箭发动机",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "engines.md" in completed.stdout
    assert "YF-21" in completed.stdout
    assert "Top hits:" in completed.stdout


def test_search_rag_reports_when_no_hits_exist(tmp_path: Path) -> None:
    data_dir = tmp_path / "RAG-data"
    data_dir.mkdir()
    (data_dir / "materials.md").write_text("# 材料\n碳纤维适用于轻量化结构。", encoding="utf-8")

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--data-dir",
            str(data_dir),
            "--query",
            "轨道机动发动机喷管烧蚀机理",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "No relevant chunks found." in completed.stdout


def test_search_rag_falls_back_from_skill_relative_data_dir(tmp_path: Path) -> None:
    project = tmp_path / "project"
    skill_scripts = project / ".clawd" / "skills" / "aircraft-design-rag" / "scripts"
    skill_scripts.mkdir(parents=True)
    data_dir = project / "RAG-data"
    data_dir.mkdir()

    resolved = search_rag.resolve_data_dir(
        skill_scripts.parent / "RAG-data",
        script_path=skill_scripts / "search_rag.py",
    )

    assert resolved == data_dir.resolve()


def test_search_rag_prioritizes_exact_designation_in_long_query() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--data-dir",
            str(ROOT / "RAG-data"),
            "--query",
            "YF-21 液体火箭发动机是什么？",
            "--top-k",
            "1",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "heading=YF-21" in completed.stdout
