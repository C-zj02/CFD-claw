"""Deterministic model-coverage registry for aircraft design intake.

The registry describes what the current Class I/II execution path can actually
evaluate.  It deliberately does not infer physical infeasibility from missing
models: an unsupported field is a model gap, not evidence that the requested
aircraft cannot exist.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from types import MappingProxyType
from typing import Any, Mapping

from src.design_intake.models import (
    DesignIntent,
    ModelCoverageRecord,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
)


CLASS_I_II_MODEL_ID = "aircraft_class_i_ii_v2"


@dataclass(frozen=True)
class CoverageDefinition:
    """Static coverage metadata keyed by a canonical requirement name."""

    status: ModelCoverageStatus
    model_id: str | None
    reason: str
    applicable_envelope: Mapping[str, Any]


def _covered(
    reason: str,
    *,
    envelope: Mapping[str, Any] | None = None,
) -> CoverageDefinition:
    return CoverageDefinition(
        status=ModelCoverageStatus.COVERED,
        model_id=CLASS_I_II_MODEL_ID,
        reason=reason,
        applicable_envelope=MappingProxyType(dict(envelope or {})),
    )


def _partial(
    reason: str,
    *,
    envelope: Mapping[str, Any] | None = None,
) -> CoverageDefinition:
    return CoverageDefinition(
        status=ModelCoverageStatus.PARTIAL,
        model_id=CLASS_I_II_MODEL_ID,
        reason=reason,
        applicable_envelope=MappingProxyType(dict(envelope or {})),
    )


def _unsupported(reason: str) -> CoverageDefinition:
    return CoverageDefinition(
        status=ModelCoverageStatus.UNSUPPORTED,
        model_id=None,
        reason=reason,
        applicable_envelope=MappingProxyType({}),
    )


# The keys are leaf-level canonical names so callers may use either the
# DesignIntent paths (for example ``mission.range_m``) or the execution request
# paths (for example ``requirements.range_m``).
MODEL_COVERAGE_MATRIX: Mapping[str, CoverageDefinition] = MappingProxyType(
    {
        "range_m": _covered("Class I/II mission range and fuel closure."),
        "payload_kg": _covered("Class I/II mass and mission closure."),
        "cruise_mach": _covered(
            "Subsonic cruise-condition aerodynamic and propulsion evaluation.",
            envelope={"minimum": 0.03, "maximum": 0.85},
        ),
        "cruise_altitude_m": _covered(
            "Cruise atmosphere, drag, thrust and mission evaluation.",
            envelope={"minimum": 0.0, "maximum": 35_000.0},
        ),
        "takeoff_distance_m": _covered("Predicted takeoff-distance hard gate."),
        "landing_distance_m": _covered("Predicted landing-distance hard gate."),
        "max_load_factor": _covered("Structural design-load input."),
        "sustained_turn_g": _covered("Sustained-turn thrust constraint."),
        "service_ceiling_m": _covered("Service-ceiling thrust constraint."),
        "aircraft_role": _covered("Task-class selection and reporting input."),
        "propulsion_type": _covered(
            "Generic jet or propeller propulsion branch.",
            envelope={"allowed": ["jet", "prop"]},
        ),
        "reserve_fraction": _covered("Mission fuel reserve hard gate."),
        "tail_layout": _covered(
            "Implemented parametric tail-layout branch.",
            envelope={"allowed": ["conventional", "t_tail", "v_tail", "twin_fin"]},
        ),
        "cl_max_takeoff": _covered("Takeoff constraint assumption."),
        "cl_max_landing": _covered("Landing constraint assumption."),
        "assumed_climb_rate_m_s": _covered("Climb and ceiling constraint assumption."),
        "uncertainty_enabled": _covered("Implemented uncertainty-analysis switch."),
        "mtow_kg": _covered("Class I weight-loop initial design variable."),
        "wing_loading_pa": _covered("Constraint-analysis design variable."),
        "thrust_to_weight": _covered("Constraint-analysis design variable."),
        "aspect_ratio": _covered("Parametric wing geometry design variable."),
        "sweep_deg": _covered("Parametric wing geometry input."),
        "taper_ratio": _covered("Parametric wing geometry input."),
        "thickness_ratio": _covered("Parametric geometry and fuel-volume input."),
        "sfc_cruise_1_s": _partial(
            "Legacy energy input is migrated at the declared cruise condition."
        ),
        "jet_tsfc_kg_per_n_s": _covered("Generic jet fuel-consumption model input."),
        "prop_bsfc_kg_per_j": _covered("Generic propeller fuel-consumption model input."),
        "prop_efficiency": _covered("Generic propeller efficiency input."),
        "cd0": _covered("Class I/II drag-polar technology assumption."),
        "oswald_e": _covered("Induced-drag technology assumption."),
        "cg_fraction_cbar": _covered("Implemented longitudinal static-margin input."),
        "horizontal_tail_volume_coefficient": _covered(
            "Implemented preliminary tail-sizing input."
        ),
        "max_mtow_kg": _partial(
            "Revalidated after weight closure; not yet a direct optimizer constraint."
        ),
        "max_aspect_ratio": _partial(
            "Revalidated after geometry closure and honored by bounded repair."
        ),
        "min_cruise_endurance_s": _unsupported(
            "The current segment mission prescribes cruise duration from the requested "
            "mission distance; it does not independently predict maximum fuel-limited "
            "cruise endurance."
        ),
        "max_flight_mach": _unsupported(
            "No maximum-speed, drag-rise, propulsion-limit and flutter validation chain is registered."
        ),
        "launch_mode": _unsupported(
            "No launch-system trajectory and aircraft-load interface model is registered."
        ),
        "launch_field_altitude_m": _unsupported(
            "Launch-site atmosphere is not coupled to a launch trajectory model."
        ),
        "booster_end_mach": _unsupported(
            "No rocket-booster separation trajectory model is registered."
        ),
        "booster_end_relative_altitude_m": _unsupported(
            "No rocket-booster separation altitude model is registered."
        ),
        "recovery_mode": _unsupported(
            "No recovery-system deployment and loads model is registered."
        ),
        "parachute_open_mach": _unsupported(
            "No parachute deployment-envelope or opening-shock model is registered."
        ),
        "parachute_open_relative_altitude_m": _unsupported(
            "No parachute descent and altitude-margin model is registered."
        ),
        "engine_count": _unsupported(
            "Generic thrust sizing is implemented, but engine installation and count are not validated."
        ),
        "configuration_reference": _unsupported(
            "Reference-aircraft styling is not converted into validated geometry constraints."
        ),
        "stealth_requirement": _unsupported(
            "No radar-cross-section, signature-control, inlet/exhaust shielding, or "
            "low-observable materials validation chain is registered."
        ),
    }
)


_PATH_ALIASES: Mapping[str, str] = MappingProxyType(
    {
        "max_mach": "max_flight_mach",
        "maximum_mach": "max_flight_mach",
        "launch.mode": "launch_mode",
        "launch.field_altitude_m": "launch_field_altitude_m",
        "launch.booster_end_mach": "booster_end_mach",
        "launch.booster_end_relative_altitude_m": "booster_end_relative_altitude_m",
        "recovery.mode": "recovery_mode",
        "recovery.parachute_open_mach": "parachute_open_mach",
        "recovery.parachute_open_relative_altitude_m": "parachute_open_relative_altitude_m",
        "propulsion.engine_count": "engine_count",
        "configuration.reference": "configuration_reference",
        "configuration.stealth_requirement": "stealth_requirement",
        "launch": "launch_mode",
        "recovery": "recovery_mode",
        "propulsion": "propulsion_type",
        "aircraft_class": "aircraft_role",
        "configuration": "tail_layout",
        "geometry.max_aspect_ratio": "max_aspect_ratio",
        "performance.max_flight_mach": "max_flight_mach",
        "performance.min_cruise_endurance_s": "min_cruise_endurance_s",
        "weights.max_mtow_kg": "max_mtow_kg",
    }
)


def canonical_coverage_key(field_path: str) -> str:
    """Normalize a requirement path to one coverage-matrix key."""

    normalized = str(field_path).strip().lower().replace("-", "_")
    for prefix in ("requirements.", "initial_guess.", "mission."):
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix) :]
            break
    aliased = _PATH_ALIASES.get(normalized)
    if aliased is not None:
        return aliased
    leaf = normalized.rsplit(".", 1)[-1]
    return _PATH_ALIASES.get(leaf, leaf)


def coverage_for_requirement(requirement: RequirementField) -> ModelCoverageRecord:
    """Return coverage evidence for one field without evaluating feasibility."""

    key = canonical_coverage_key(requirement.path)
    definition = MODEL_COVERAGE_MATRIX.get(key)
    if definition is None:
        definition = _unsupported(
            "No deterministic model-coverage record is registered for this field."
        )

    status = definition.status
    reason = definition.reason
    envelope = dict(definition.applicable_envelope)
    value = requirement.value
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and (
            ("minimum" in envelope and float(value) < float(envelope["minimum"]))
            or ("maximum" in envelope and float(value) > float(envelope["maximum"]))
        )
    ):
        status = ModelCoverageStatus.UNSUPPORTED
        reason = (
            f"The declared value {value!r} is outside the registered model envelope; "
            "this is a model-applicability gap, not a physical infeasibility finding."
        )
    allowed = envelope.get("allowed")
    if allowed is not None and value not in allowed:
        status = ModelCoverageStatus.UNSUPPORTED
        reason = (
            f"The declared value {value!r} is outside the registered categorical model "
            "envelope; this is a model-applicability gap."
        )

    role_value = getattr(requirement.role, "value", requirement.role)
    blocking = status is ModelCoverageStatus.UNSUPPORTED and (
        bool(requirement.locked) or role_value != RequirementRole.SOFT_GOAL.value
    )
    return ModelCoverageRecord(
        field_path=requirement.path,
        status=status,
        model_id=definition.model_id,
        reason=reason,
        applicable_envelope=envelope,
        blocking=blocking,
    )


def assess_model_coverage(intent: DesignIntent) -> tuple[ModelCoverageRecord, ...]:
    """Assess every declared field in stable input order."""

    requirements = list(intent.requirements)
    represented = {canonical_coverage_key(item.path) for item in requirements}
    explicit_paths = {item.path for item in requirements}
    # Top-level intent categories preserve natural-language structure.  Add
    # coverage evidence when a parser has not also emitted a RequirementField.
    for path, value, key in (
        ("aircraft_class", intent.aircraft_class, "aircraft_role"),
        ("configuration", intent.configuration, "tail_layout"),
        ("propulsion", intent.propulsion, "propulsion_type"),
        ("launch", intent.launch, "launch_mode"),
        ("recovery", intent.recovery, "recovery_mode"),
    ):
        if value is None or key in represented:
            continue
        # The parser also uses ``configuration`` for a human-readable
        # reference label.  Its explicit soft-goal field is authoritative and
        # must not be reinterpreted as a locked tail-layout requirement.
        if path == "configuration" and "configuration.reference" in explicit_paths:
            continue
        requirements.append(
            RequirementField(
                path=path,
                value=value,
                role=RequirementRole.HARD_CONSTRAINT,
                locked=True,
            )
        )
        represented.add(key)
    return tuple(coverage_for_requirement(item) for item in requirements)


def coverage_matrix_as_dict() -> dict[str, dict[str, Any]]:
    """Return a JSON-safe snapshot for API discovery and diagnostics."""

    return {
        key: {
            "status": definition.status.value,
            "model_id": definition.model_id,
            "reason": definition.reason,
            "applicable_envelope": dict(definition.applicable_envelope),
        }
        for key, definition in MODEL_COVERAGE_MATRIX.items()
    }


__all__ = [
    "CLASS_I_II_MODEL_ID",
    "CoverageDefinition",
    "MODEL_COVERAGE_MATRIX",
    "assess_model_coverage",
    "canonical_coverage_key",
    "coverage_for_requirement",
    "coverage_matrix_as_dict",
]
