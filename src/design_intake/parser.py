"""Deterministic first-pass parsing for aircraft-design conversations.

The parser intentionally covers high-value requirement phrases and preserves
unknown text for later clarification. It is not allowed to invent engineering
assumptions: every emitted requirement field is explicit in the request.
"""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import replace
from typing import Any, Callable, Match

from .models import (
    DesignIntent,
    DesignIntentStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)


PARSER_VERSION = 1

_NUMBER = r"([0-9]+(?:\.[0-9]+)?)"
_SOFT_MARKERS = ("参考", "尽量", "优先", "建议", "目标", "大约", "约为", "可选")
_HARD_BOUND_MARKERS = (
    "不大于",
    "不得超过",
    "不超过",
    "至多",
    "不低于",
    "不少于",
    "至少",
    "<=",
    ">=",
    "≤",
    "≥",
)
_CHANGE_MARKERS = (
    "改为",
    "改成",
    "修改为",
    "调整为",
    "调整成",
    "降低到",
    "提高到",
    "增加到",
    "减少到",
    "更新为",
    "change to",
    "set to",
    "update to",
)


def looks_like_design_request(text: str) -> bool:
    """Return whether text appears to request an aircraft design calculation."""

    if not isinstance(text, str):
        return False
    normalized = text.strip().lower()
    if not normalized:
        return False
    subject = any(term in normalized for term in ("飞机", "飞行器", "无人机", "uav", "aircraft"))
    action = any(term in normalized for term in ("设计", "方案", "总体参数", "sizing"))
    engineering_field = any(
        term in normalized
        for term in ("航程", "航时", "载荷", "马赫", "mach", "升限", "起飞重量", "mtow")
    )
    explanatory = any(
        term in normalized
        for term in ("解释", "介绍", "原理", "教程", "为什么", "怎么优化", "如何优化")
    )
    if explanatory and not engineering_field:
        return False
    return subject and action


def looks_like_requirement_change(text: str) -> bool:
    """Return whether text explicitly asks to change a numerical baseline field."""

    if not isinstance(text, str):
        return False
    normalized = text.strip().lower()
    if not normalized or not any(marker in normalized for marker in _CHANGE_MARKERS):
        return False
    try:
        parsed = parse_design_intent(normalized)
    except ValueError:
        return False
    return any(field.source is RequirementSource.USER for field in parsed.requirements)


def _context_is_soft(text: str, start: int) -> bool:
    context = text[max(0, start - 14) : start]
    return any(marker in context for marker in _SOFT_MARKERS)


def _mass_kg(value: str, unit: str | None) -> float:
    parsed = float(value)
    normalized = (unit or "kg").lower()
    return parsed * 1_000.0 if normalized in {"t", "吨", "ton", "tonne"} else parsed


def _distance_m(value: str, unit: str | None) -> float:
    parsed = float(value)
    normalized = (unit or "m").lower()
    return parsed * 1_000.0 if normalized in {"km", "公里", "千米"} else parsed


def _duration_s(value: str, unit: str | None) -> float:
    parsed = float(value)
    normalized = (unit or "h").lower()
    if normalized in {"h", "hr", "hour", "小时", "时"}:
        return parsed * 3_600.0
    if normalized in {"min", "minute", "分钟", "分"}:
        return parsed * 60.0
    return parsed


def _speed_of_sound_m_s(altitude_m: float) -> float:
    """Return ISA speed of sound through the lower stratosphere."""

    bounded_altitude = min(20_000.0, max(0.0, altitude_m))
    temperature_k = (
        288.15 - 0.0065 * bounded_altitude
        if bounded_altitude <= 11_000.0
        else 216.65
    )
    return math.sqrt(1.4 * 287.05287 * temperature_k)


def _explicit_field(
    *,
    path: str,
    value: Any,
    unit: str | None,
    soft: bool = False,
    confidence: float = 1.0,
) -> RequirementField:
    return RequirementField(
        path=path,
        value=value,
        unit=unit,
        role=RequirementRole.SOFT_GOAL if soft else RequirementRole.HARD_CONSTRAINT,
        locked=not soft,
        source=RequirementSource.USER,
        confidence=confidence,
    )


def parse_design_intent(text: str, *, intent_id: str | None = None) -> DesignIntent:
    """Parse explicit Chinese/English sizing requirements into a DesignIntent.

    Missing values remain missing so the preflight layer can ask focused
    questions. No generic aircraft or propulsion defaults are introduced here.
    """

    if not isinstance(text, str):
        raise ValueError("design request must be a string")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("design request must not be empty")
    if len(cleaned) > 20_000:
        raise ValueError("design request must be at most 20000 characters")
    original_text = cleaned
    for marker in _CHANGE_MARKERS:
        cleaned = cleaned.replace(marker, "为")

    fields: dict[str, RequirementField] = {}

    def capture(
        path: str,
        pattern: str,
        converter: Callable[[str, str | None], Any],
        unit: str | None,
        *,
        flags: int = re.IGNORECASE,
        value_group: int = 1,
        unit_group: int | None = 2,
        soft: bool | None = None,
    ) -> Match[str] | None:
        match = re.search(pattern, cleaned, flags=flags)
        if match is None:
            return None
        raw_unit = match.group(unit_group) if unit_group is not None else None
        is_soft = _context_is_soft(cleaned, match.start()) if soft is None else soft
        if soft is None and any(marker in match.group(0) for marker in _HARD_BOUND_MARKERS):
            is_soft = False
        fields[path] = _explicit_field(
            path=path,
            value=converter(match.group(value_group), raw_unit),
            unit=unit,
            soft=is_soft,
        )
        return match

    capture(
        "weights.max_mtow_kg",
        rf"(?:最大起飞(?:重量|质量)|\bmtow\b)\s*(?:不大于|不得超过|不超过|至多|<=|≤|为|[:：])?\s*{_NUMBER}\s*(kg|公斤|千克|t|吨)?",
        _mass_kg,
        "kg",
    )
    capture(
        "requirements.payload_kg",
        rf"(?:任务载荷|有效载荷|载荷|载重)\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}\s*(kg|公斤|千克|t|吨)?",
        _mass_kg,
        "kg",
    )
    capture(
        "requirements.range_m",
        rf"(?:设计)?(?:航程|任务距离)\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
        _distance_m,
        "m",
    )
    capture(
        "requirements.cruise_altitude_m",
        rf"(?:设计)?巡航高度\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
        _distance_m,
        "m",
    )
    capture(
        "requirements.cruise_mach",
        rf"(?:设计)?巡航(?:马赫数|\s*mach|\s*ma)\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}",
        lambda value, _unit: float(value),
        "Mach",
        unit_group=None,
    )
    capture(
        "performance.min_cruise_endurance_s",
        rf"(?:巡航航时|巡航时间|续航时间|航时)\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}\s*(h|hr|hour|小时|时|min|分钟|分|s|秒)?",
        _duration_s,
        "s",
    )
    capture(
        "performance.max_flight_mach",
        rf"(?:设计)?最大(?:飞行)?(?:马赫数|\s*mach|\s*ma)\s*(?:不大于|不得超过|不超过|至多|<=|≤|为|[:：])?\s*{_NUMBER}",
        lambda value, _unit: float(value),
        "Mach",
        unit_group=None,
    )
    capture(
        "requirements.service_ceiling_m",
        rf"(?:实用|使用|设计)?升限\s*(?:不低于|不少于|至少|>=|≥|为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
        _distance_m,
        "m",
    )
    capture(
        "geometry.max_aspect_ratio",
        rf"展弦比\s*(?:不大于|不得超过|不超过|至多|<=|≤|为|[:：])?\s*{_NUMBER}",
        lambda value, _unit: float(value),
        "ratio",
        unit_group=None,
    )
    capture(
        "launch.field_altitude_m",
        rf"(?:发射场|起飞场|机场)(?:海拔|高度)\s*(?:为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
        _distance_m,
        "m",
    )

    booster_clause = re.search(r"(?:火箭)?助推结束[^。；;\n]{0,100}", cleaned, re.IGNORECASE)
    if booster_clause is not None:
        clause = booster_clause.group(0)
        mach = re.search(rf"(?:马赫数|mach|ma)\s*(?:为|[:：])?\s*{_NUMBER}", clause, re.IGNORECASE)
        altitude = re.search(
            rf"相对高度\s*(?:为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
            clause,
            re.IGNORECASE,
        )
        if mach is not None:
            fields["launch.booster_end_mach"] = _explicit_field(
                path="launch.booster_end_mach",
                value=float(mach.group(1)),
                unit="Mach",
            )
        if altitude is not None:
            fields["launch.booster_end_relative_altitude_m"] = _explicit_field(
                path="launch.booster_end_relative_altitude_m",
                value=_distance_m(altitude.group(1), altitude.group(2)),
                unit="m",
            )

    parachute_clause = re.search(r"(?:开伞|降落伞打开)[^。；;\n]{0,100}", cleaned, re.IGNORECASE)
    if parachute_clause is not None:
        clause = parachute_clause.group(0)
        mach = re.search(rf"(?:速度\s*)?(?:马赫数|mach|ma)?\s*{_NUMBER}", clause, re.IGNORECASE)
        altitude = re.search(
            rf"相对高度\s*(?:为|[:：])?\s*{_NUMBER}\s*(km|公里|千米|m|米)?",
            clause,
            re.IGNORECASE,
        )
        if mach is not None:
            fields["recovery.parachute_open_mach"] = _explicit_field(
                path="recovery.parachute_open_mach",
                value=float(mach.group(1)),
                unit="Mach",
            )
        if altitude is not None:
            fields["recovery.parachute_open_relative_altitude_m"] = _explicit_field(
                path="recovery.parachute_open_relative_altitude_m",
                value=_distance_m(altitude.group(1), altitude.group(2)),
                unit="m",
            )

    launch: str | None = None
    if "火箭助推" in cleaned or "rocket assist" in cleaned.lower():
        launch = "rocket_assist"
        fields["launch.mode"] = _explicit_field(
            path="launch.mode",
            value=launch,
            unit=None,
        )

    recovery: str | None = None
    if "伞降" in cleaned or "降落伞" in cleaned or "parachute" in cleaned.lower():
        recovery = "parachute"
        fields["recovery.mode"] = _explicit_field(
            path="recovery.mode",
            value=recovery,
            unit=None,
        )

    engine_count: int | None = None
    if re.search(r"(?:采用|使用|布局为|布局)?\s*单发(?:动机)?", cleaned):
        engine_count = 1
    elif re.search(r"(?:采用|使用|布局为|布局)?\s*双发(?:动机)?", cleaned):
        engine_count = 2
    if engine_count is not None:
        fields["propulsion.engine_count"] = _explicit_field(
            path="propulsion.engine_count",
            value=engine_count,
            unit="count",
        )

    propulsion: str | None = None
    if re.search(r"涡喷|喷气|turbojet|\bjet\b", cleaned, re.IGNORECASE):
        propulsion = "jet"
    elif re.search(r"螺旋桨|活塞|propeller|\bprop\b", cleaned, re.IGNORECASE):
        propulsion = "prop"
    if propulsion is not None:
        fields["requirements.propulsion_type"] = _explicit_field(
            path="requirements.propulsion_type",
            value=propulsion,
            unit=None,
        )

    reference_match = re.search(
        r"(?:布局风格\s*)?(?:可)?参考\s*([^，。,.;；\n]+)",
        cleaned,
        re.IGNORECASE,
    )
    configuration: str | None = None
    if reference_match is not None:
        configuration = reference_match.group(1).strip()
        fields["configuration.reference"] = _explicit_field(
            path="configuration.reference",
            value=configuration,
            unit=None,
            soft=True,
        )

    if re.search(r"隐身|低可探测|低可观测|\bstealth\b|low[- ]observable", cleaned, re.IGNORECASE):
        fields["configuration.stealth_requirement"] = _explicit_field(
            path="configuration.stealth_requirement",
            value=True,
            unit=None,
        )

    diagnostic_fields: list[str] = []
    range_field = fields.get("requirements.range_m")
    endurance_field = fields.get("performance.min_cruise_endurance_s")
    mach_field = fields.get("requirements.cruise_mach")
    altitude_field = fields.get("requirements.cruise_altitude_m")
    minimum_cruise_segment_distance_m: float | None = None
    if range_field is None and endurance_field and mach_field and altitude_field:
        minimum_cruise_segment_distance_m = (
            float(mach_field.value)
            * _speed_of_sound_m_s(float(altitude_field.value))
            * float(endurance_field.value)
        )
        diagnostic_fields.append("mission.minimum_cruise_segment_distance_m")

    digest = hashlib.sha256(original_text.encode("utf-8")).hexdigest()[:16]
    resolved_id = intent_id or f"design-intent-{digest}"
    aircraft_class = "fixed_wing_uav" if any(term in cleaned.lower() for term in ("无人机", "uav")) else None
    mission = {
        "declared_field_count": len(fields),
        "derived_fields": (),
        "diagnostic_fields": diagnostic_fields,
    }
    if minimum_cruise_segment_distance_m is not None:
        mission["minimum_cruise_segment_distance_m"] = minimum_cruise_segment_distance_m
        mission["minimum_cruise_segment_distance_basis"] = (
            "Mach * ISA speed of sound at cruise altitude * minimum cruise endurance. "
            "This is a cruise-segment distance diagnostic, not total mission range."
        )
    return DesignIntent(
        intent_id=resolved_id,
        requirements=tuple(fields.values()),
        status=DesignIntentStatus.NEEDS_CLARIFICATION,
        original_request=original_text,
        mission=mission,
        aircraft_class=aircraft_class,
        configuration=configuration,
        propulsion=propulsion,
        launch=launch,
        recovery=recovery,
        metadata={
            "parser": {"name": "deterministic_aircraft_request_parser", "version": PARSER_VERSION},
            "input_language": "zh" if re.search(r"[\u4e00-\u9fff]", cleaned) else "unknown",
        },
    )


def with_intent_status(intent: DesignIntent, status: DesignIntentStatus | str) -> DesignIntent:
    """Return an intent carrying a diagnosis state without mutating its revision."""

    return replace(intent, status=DesignIntentStatus(status))


__all__ = [
    "PARSER_VERSION",
    "looks_like_design_request",
    "looks_like_requirement_change",
    "parse_design_intent",
    "with_intent_status",
]
