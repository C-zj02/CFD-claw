from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?\s*(?:%|kg|km|m²|m\^2|m/s|km/h|kW|shp|N|g|°)?")
PATH_RE = re.compile(r"(?P<path>(?:/[\w.\-\u4e00-\u9fff ]+)+\.(?:svg|csv|json|png|md))")

DIMENSIONS: dict[str, list[str]] = {
    "需求解析": ["需求", "用户输入", "航程", "载荷", "任务"],
    "任务剖面": ["任务剖面", "起飞", "爬升", "巡航", "下降", "着陆"],
    "总体参数": ["起飞重量", "空机", "燃油", "翼面积", "翼展", "翼载荷", "推重比"],
    "约束分析": ["约束", "起飞距离", "着陆距离", "爬升", "CLmax", "W/S", "T/W"],
    "布局方案": ["布局", "机翼", "机身", "尾翼", "起落架", "动力", "涡桨"],
    "迭代闭合": ["V0", "V1", "V2", "闭合", "迭代", "回算"],
    "依据追溯": ["依据", "检索", "RAG", "本地", "来源", "文件"],
    "图表文件": ["方案界限线图", ".svg", ".csv", "路径", "设计点"],
    "校核结果": ["校核", "通过", "裕度", "可行", "计算结果"],
    "风险验证": ["风险", "下一步", "验证", "CFD", "风洞", "MDAO"],
}


def evaluate_aircraft_response(response: Any, rubric_path: Path) -> tuple[bool, dict[str, Any], float, None]:
    rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
    answer = extract_answer(response)
    process = extract_process(response)
    checks = [
        check_basic(answer),
        check_expected_terms(answer, rubric.get("expected_terms", [])),
        check_required_dimensions(answer, rubric.get("required_dimensions", [])),
        check_quantitative(answer, rubric.get("min_numbers", 3)),
        check_traceability(answer),
        check_artifacts(answer, bool(rubric.get("artifact_expected"))),
        check_output_constraints(answer, bool(rubric.get("concise_expected"))),
        check_process_visibility(answer, process),
    ]
    total = sum(check["score"] for check in checks)
    max_total = sum(check["max_score"] for check in checks)
    score = round(total / max_total * 100, 2) if max_total else 0.0
    pass_score = float(rubric.get("pass_score", 70))
    passed = score >= pass_score
    detail = {
        "task_id": rubric.get("task_id"),
        "score": score,
        "pass_score": pass_score,
        "answer_chars": len(answer),
        "process_chars": len(process),
        "checks": checks,
        "missing_expected_terms": missing_terms(answer, rubric.get("expected_terms", [])),
    }
    return passed, detail, score, None


def extract_answer(response: Any) -> str:
    if isinstance(response, str):
        return response.strip()
    if isinstance(response, dict):
        return str(response.get("answer") or response.get("response") or "").strip()
    return str(getattr(response, "answer", "") or getattr(response, "response", "") or response).strip()


def extract_process(response: Any) -> str:
    if isinstance(response, dict):
        return str(response.get("agent_process_output") or response.get("process") or "")
    return str(getattr(response, "agent_process_output", "") or getattr(response, "process", "") or "")


def check_basic(answer: str) -> dict[str, Any]:
    score = 0.0
    score += 4 if answer else 0
    score += 3 if len(answer) >= 120 else 0
    score += 3 if contains_any(answer, ["飞行器", "无人机", "机翼", "航程", "载荷", "设计"]) else 0
    return result("基础可读性", score, 10, score >= 7, f"answer_chars={len(answer)}")


def check_expected_terms(answer: str, terms: list[str]) -> dict[str, Any]:
    hits = count_hits(answer, terms)
    score = 20 * hits / max(1, len(terms))
    return result("题目要点覆盖", score, 20, score >= 14, f"hits={hits}/{len(terms)}")


def check_required_dimensions(answer: str, dimensions: list[str]) -> dict[str, Any]:
    if not dimensions:
        dimensions = list(DIMENSIONS)
    covered = [name for name in dimensions if contains_any(answer, DIMENSIONS.get(name, [name]))]
    score = 25 * len(covered) / max(1, len(dimensions))
    return result("工程维度覆盖", score, 25, score >= 17.5, "covered=" + "、".join(covered))


def check_quantitative(answer: str, min_numbers: int) -> dict[str, Any]:
    numbers = NUMBER_RE.findall(answer)
    unit_hits = count_hits(answer, ["kg", "km", "m²", "m^2", "m/s", "km/h", "kW", "W/S", "T/W", "CLmax", "%"])
    formula_hits = count_hits(answer, ["W/S", "T/W", "CLmax", "V0", "V1", "V2", "L/D", "Breguet"])
    score = min(6, len(numbers) / max(1, min_numbers) * 6) + min(5, unit_hits) + min(4, formula_hits)
    return result("数值单位与公式", score, 15, score >= 9, f"numbers={len(numbers)}, unit_hits={unit_hits}, formula_hits={formula_hits}")


def check_traceability(answer: str) -> dict[str, Any]:
    groups = [
        ("依据", ["依据", "来源", "检索", "RAG", "本地知识库"]),
        ("假设", ["工程假设", "假设", "用户给定", "用户输入"]),
        ("校核", ["校核", "计算", "闭合", "通过", "裕度"]),
        ("风险", ["风险", "下一步", "验证", "CFD", "风洞"]),
    ]
    covered = [name for name, terms in groups if contains_any(answer, terms)]
    score = 15 * len(covered) / len(groups)
    return result("工程可追溯性", score, 15, score >= 9, "covered=" + "、".join(covered))


def check_artifacts(answer: str, expected: bool) -> dict[str, Any]:
    paths = [match.group("path") for match in PATH_RE.finditer(answer)]
    existing = [path for path in paths if Path(path).exists()]
    has_svg = ".svg" in answer.lower()
    has_csv = ".csv" in answer.lower()
    if not expected:
        score = 10 if not paths or existing else 7
        return result("图表文件", score, 10, score >= 7, f"paths={len(paths)}, existing={len(existing)}")
    score = 0.0
    score += 3 if has_svg else 0
    score += 3 if has_csv else 0
    score += 2 if paths else 0
    score += 2 if existing else 0
    return result("图表文件", score, 10, score >= 7, f"has_svg={has_svg}, has_csv={has_csv}, paths={len(paths)}, existing={len(existing)}")


def check_output_constraints(answer: str, concise_expected: bool) -> dict[str, Any]:
    if not concise_expected:
        return result("输出约束", 5, 5, True, "无特殊长度约束")
    score = 5 if len(answer) <= 1600 else 2
    return result("输出约束", score, 5, score >= 4, f"要求简洁，answer_chars={len(answer)}")


def check_process_visibility(answer: str, process: str) -> dict[str, Any]:
    score = 5 if process else 0
    if score == 0 and contains_any(answer, ["设计推理记录", "推理", "依据", "取舍"]):
        score = 3
    return result("过程可见性", score, 5, score >= 3, f"process_chars={len(process)}")


def result(name: str, score: float, max_score: float, passed: bool, detail: str) -> dict[str, Any]:
    return {
        "name": name,
        "score": round(score, 2),
        "max_score": max_score,
        "passed": passed,
        "detail": detail,
    }


def contains_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def count_hits(text: str, terms: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def missing_terms(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    return [term for term in terms if term.lower() not in lowered]
