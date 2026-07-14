"""Natural-language intake regressions for aircraft design requests."""

from __future__ import annotations

from src.design_intake.models import RequirementRole, RequirementSource
from src.design_intake.parser import (
    looks_like_design_request,
    looks_like_requirement_change,
    parse_design_intent,
)


STEALTH_UAV_REQUEST = (
    "设计一款隐身作战无人机，要求最大起飞重量不大于260kg，任务载荷60kg，"
    "设计巡航高度9.5km，巡航马赫数0.6，要求巡航航时不低于1h，"
    "设计最大飞行马赫数0.8，使用升限10km，采用火箭助推+伞降回收形式，"
    "发射场海拔1500m，火箭助推结束为马赫数0.28、相对高度40m，"
    "开伞速度Ma0.24，相对高度1000m，采用单发布局形式，"
    "布局风格可参考沙赫德-136无人机，展弦比不大于2.5。"
)


def test_parser_extracts_complex_uav_requirements_without_inventing_defaults() -> None:
    intent = parse_design_intent(STEALTH_UAV_REQUEST)

    assert intent.aircraft_class == "fixed_wing_uav"
    assert intent.launch == "rocket_assist"
    assert intent.recovery == "parachute"
    assert intent.requirement("weights.max_mtow_kg").value == 260.0
    assert intent.requirement("requirements.payload_kg").value == 60.0
    assert intent.requirement("requirements.cruise_altitude_m").value == 9_500.0
    assert intent.requirement("requirements.cruise_mach").value == 0.6
    assert intent.requirement("performance.min_cruise_endurance_s").value == 3_600.0
    assert intent.requirement("performance.max_flight_mach").value == 0.8
    assert intent.requirement("requirements.service_ceiling_m").value == 10_000.0
    assert intent.requirement("launch.field_altitude_m").value == 1_500.0
    assert intent.requirement("launch.booster_end_mach").value == 0.28
    assert intent.requirement("launch.booster_end_relative_altitude_m").value == 40.0
    assert intent.requirement("recovery.parachute_open_mach").value == 0.24
    assert intent.requirement("recovery.parachute_open_relative_altitude_m").value == 1_000.0
    assert intent.requirement("propulsion.engine_count").value == 1
    assert intent.requirement("geometry.max_aspect_ratio").value == 2.5
    stealth = intent.requirement("configuration.stealth_requirement")
    assert stealth.value is True
    assert stealth.role is RequirementRole.HARD_CONSTRAINT
    assert stealth.locked is True
    reference = intent.requirement("configuration.reference")
    assert reference.role is RequirementRole.SOFT_GOAL
    assert reference.locked is False
    assert "沙赫德-136" in reference.value
    assert all(field.source is not RequirementSource.DEFAULT for field in intent.requirements)
    assert "requirements.takeoff_distance_m" not in {field.path for field in intent.requirements}


def test_parser_keeps_cruise_distance_as_diagnostic_and_requests_total_range() -> None:
    intent = parse_design_intent(STEALTH_UAV_REQUEST)
    paths = {field.path for field in intent.requirements}

    assert "requirements.range_m" not in paths
    assert intent.mission["derived_fields"] == ()
    assert intent.mission["diagnostic_fields"] == (
        "mission.minimum_cruise_segment_distance_m",
    )
    assert 630_000.0 < intent.mission["minimum_cruise_segment_distance_m"] < 670_000.0
    assert "not total mission range" in intent.mission[
        "minimum_cruise_segment_distance_basis"
    ]


def test_parser_preserves_explicit_range_instead_of_rederiving_it() -> None:
    intent = parse_design_intent(
        "设计一款无人机，航程至少800km，载荷30kg，巡航高度5km，"
        "巡航马赫数0.3，巡航航时至少1h。"
    )

    range_field = intent.requirement("requirements.range_m")
    assert range_field.value == 800_000.0
    assert range_field.source is RequirementSource.USER
    assert range_field.locked is True


def test_parser_leaves_missing_engineering_choices_for_clarification() -> None:
    intent = parse_design_intent("设计一款无人机，航程500km，载荷20kg。")
    paths = {field.path for field in intent.requirements}

    assert "requirements.propulsion_type" not in paths
    assert "requirements.cruise_mach" not in paths
    assert "requirements.cruise_altitude_m" not in paths


def test_explicit_bound_is_not_softened_by_nearby_reference_language() -> None:
    intent = parse_design_intent(
        "设计一款无人机，航程500km，载荷20kg，布局风格可参考某型无人机，"
        "展弦比不大于2.5。"
    )

    aspect_ratio = intent.requirement("geometry.max_aspect_ratio")
    assert aspect_ratio.role is RequirementRole.HARD_CONSTRAINT
    assert aspect_ratio.locked is True


def test_design_request_detector_avoids_general_skill_questions() -> None:
    assert looks_like_design_request(STEALTH_UAV_REQUEST) is True
    assert looks_like_design_request("这个总体设计技能为什么总显示不可行？") is False
    assert looks_like_design_request("请解释一下飞机升力公式") is False


def test_requirement_change_detector_requires_an_explicit_changed_value() -> None:
    assert looks_like_requirement_change("把载荷改为50kg") is True
    assert looks_like_requirement_change("将航程降低到400km") is True
    assert looks_like_requirement_change("我想修改一下这个方案") is False
    assert looks_like_requirement_change("为什么要降低载荷？") is False

    parsed = parse_design_intent("把载荷改成50kg")
    assert parsed.original_request == "把载荷改成50kg"
    assert parsed.requirement("requirements.payload_kg").value == 50.0
