"""Bounded, auditable repair proposals for infeasible aircraft designs."""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass, replace
from typing import Any

from src.design_execution.models import (
    AircraftDesignEngineeringResult,
    AircraftDesignRequest,
)


@dataclass(frozen=True)
class AircraftDesignRepairProposal:
    request: AircraftDesignRequest
    record: dict[str, Any]


_BOUNDS: dict[str, tuple[float, float]] = {
    "mtow_kg": (1.0, 2_000_000.0),
    "wing_loading_pa": (50.0, 20_000.0),
    "thrust_to_weight": (0.02, 3.0),
    "aspect_ratio": (1.0, 40.0),
    "thickness_ratio": (0.03, 0.30),
    "jet_tsfc_kg_per_n_s": (1e-9, 0.001),
    "prop_bsfc_kg_per_j": (1e-10, 1e-5),
    "prop_efficiency": (0.1, 1.0),
    "cd0": (0.001, 0.30),
    "oswald_e": (0.1, 1.2),
    "cg_fraction_cbar": (0.05, 0.55),
    "horizontal_tail_volume_coefficient": (0.1, 1.5),
}


def _finite(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _user_aspect_ratio_limit(request: AircraftDesignRequest) -> float | None:
    provenance = request.provenance
    candidates = [
        provenance.get("user_requirements"),
        provenance.get("user_provenance", {}).get("user_requirements")
        if isinstance(provenance.get("user_provenance"), dict)
        else None,
    ]
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        value = _finite(candidate.get("max_aspect_ratio"))
        if value is not None:
            return value
    return None


def propose_aircraft_design_repair(
    request: AircraftDesignRequest,
    engineering: AircraftDesignEngineeringResult | None,
    design_data: dict[str, Any] | None,
    *,
    repair_attempt: int,
) -> AircraftDesignRepairProposal | None:
    """Return one bounded design-variable repair without changing requirements."""

    if engineering is None:
        return None
    failed = [
        item
        for item in engineering.constraints
        if item.get("blocking") is True and item.get("passed") is False
    ]
    failed_by_id = {str(item.get("id")): item for item in failed}
    failed_ids = sorted(failed_by_id)
    initial = request.initial_guess
    targets = initial.to_dict()
    action_reasons: dict[str, list[str]] = {}
    action_triggers: dict[str, set[str]] = {}

    def propose(field: str, value: float, reason: str, trigger_ids: list[str]) -> None:
        lower, upper = _BOUNDS[field]
        if field == "aspect_ratio":
            user_limit = _user_aspect_ratio_limit(request)
            if user_limit is not None:
                upper = min(upper, user_limit)
        bounded = min(upper, max(lower, float(value)))
        current = _finite(targets.get(field))
        if current is None or math.isclose(current, bounded, rel_tol=1e-9, abs_tol=1e-12):
            return
        targets[field] = bounded
        action_reasons.setdefault(field, []).append(reason)
        action_triggers.setdefault(field, set()).update(trigger_ids)

    thrust_ids = [
        constraint_id
        for constraint_id in failed_ids
        if constraint_id
        in {
            "class1.takeoff_distance",
            "class1.sustained_turn_thrust",
            "class1.service_ceiling_thrust",
            "advanced.propulsion.cruise_thrust_margin",
            "advanced.propulsion.climb_thrust_margin",
        }
    ]
    if thrust_ids:
        deficit = max(
            [
                abs(_finite(failed_by_id[item].get("margin")) or 0.0)
                for item in thrust_ids
            ]
            or [0.0]
        )
        propose(
            "thrust_to_weight",
            max(initial.thrust_to_weight * 1.15, initial.thrust_to_weight + deficit * 1.15 + 0.02),
            "Increase installed thrust margin for failed performance gates.",
            thrust_ids,
        )

    landing_ids = [item for item in failed_ids if item == "class1.landing_distance"]
    if landing_ids:
        constraint = failed_by_id[landing_ids[0]]
        required = _finite(constraint.get("required"))
        actual = _finite(constraint.get("actual"))
        ratio = required / actual if required and actual and actual > 0.0 else 0.85
        propose(
            "wing_loading_pa",
            initial.wing_loading_pa * min(0.95, max(0.65, ratio * 0.95)),
            "Reduce wing loading to meet landing-distance demand.",
            landing_ids,
        )

    mission_ids = [
        item
        for item in failed_ids
        if item
        in {
            "class1.range",
            "class1.fuel_fraction",
            "advanced.mission.fuel_capacity",
            "declared.max_mtow_kg",
        }
    ]
    if mission_ids:
        propose(
            "aspect_ratio",
            initial.aspect_ratio * 1.12,
            "Increase aerodynamic efficiency for mission fuel and range closure.",
            mission_ids,
        )
        propose(
            "cd0",
            initial.cd0 * 0.90,
            "Reduce zero-lift drag within the declared technology envelope.",
            mission_ids,
        )
        propose(
            "oswald_e",
            initial.oswald_e * 1.04,
            "Improve span efficiency within the bounded design-variable range.",
            mission_ids,
        )
        energy_field = (
            "jet_tsfc_kg_per_n_s"
            if request.requirements.propulsion_type == "jet"
            else "prop_bsfc_kg_per_j"
        )
        energy_value = _finite(targets.get(energy_field))
        if energy_value is not None:
            propose(
                energy_field,
                energy_value * 0.94,
                "Improve propulsion fuel consumption within the bounded assumption range.",
                mission_ids,
            )

    stability_ids = [
        item for item in failed_ids if item == "advanced.stability.static_margin_min"
    ]
    if stability_ids:
        constraint = failed_by_id[stability_ids[0]]
        required = _finite(constraint.get("required")) or 0.05
        actual = _finite(constraint.get("actual"))
        shortfall = required - actual if actual is not None else 0.05
        propose(
            "cg_fraction_cbar",
            initial.cg_fraction_cbar - max(0.02, shortfall + 0.015),
            "Move the design CG forward to recover positive static margin.",
            stability_ids,
        )
        propose(
            "horizontal_tail_volume_coefficient",
            initial.horizontal_tail_volume_coefficient * 1.08,
            "Increase horizontal-tail effectiveness for static stability.",
            stability_ids,
        )

    structure_ids = [
        item for item in failed_ids if item == "advanced.structures.weight_feedback"
    ]
    if structure_ids:
        propose(
            "wing_loading_pa",
            initial.wing_loading_pa * 0.90,
            "Reduce structural loading for the advanced wingbox check.",
            structure_ids,
        )
        propose(
            "thickness_ratio",
            initial.thickness_ratio * 1.10,
            "Increase available wingbox depth for structural efficiency.",
            structure_ids,
        )

    geometry_ids = [
        item for item in failed_ids if item == "advanced.geometry.fuel_volume"
    ]
    if geometry_ids:
        propose(
            "thickness_ratio",
            initial.thickness_ratio * 1.15,
            "Increase usable fuel volume within the thickness-ratio bound.",
            geometry_ids,
        )
        propose(
            "wing_loading_pa",
            initial.wing_loading_pa * 0.85,
            "Increase wing area to recover fuel-volume capacity.",
            geometry_ids,
        )

    aspect_ids = [
        item
        for item in failed_ids
        if item in {"advanced.geometry.aspect_ratio_limit", "declared.max_aspect_ratio"}
    ]
    if aspect_ids:
        required = _finite(failed_by_id[aspect_ids[0]].get("required"))
        if required is not None:
            propose(
                "aspect_ratio",
                required,
                "Clamp aspect ratio to the active geometry limit.",
                aspect_ids,
            )

    next_max_iterations = request.max_iterations
    if engineering.numerical_converged is False or "class1.weight_closure" in failed_by_id:
        history = engineering.iteration_history
        if not history and isinstance(design_data, dict):
            candidate_history = design_data.get("iteration_history")
            history = candidate_history if isinstance(candidate_history, list) else []
        if history and isinstance(history[-1], dict):
            last_mtow = _finite(
                history[-1].get("calculated_mtow", history[-1].get("mtow"))
            )
            if last_mtow is not None:
                propose(
                    "mtow_kg",
                    last_mtow,
                    "Restart the fixed-point loop from the latest finite weight estimate.",
                    ["class1.weight_closure"],
                )
        next_max_iterations = min(500, max(request.max_iterations + 10, request.max_iterations * 2))

    if not action_reasons and next_max_iterations == request.max_iterations:
        return None

    updated_initial = replace(initial, **targets)
    actions = []
    for field in sorted(action_reasons):
        lower, upper = _BOUNDS[field]
        if field == "aspect_ratio":
            user_limit = _user_aspect_ratio_limit(request)
            if user_limit is not None:
                upper = min(upper, user_limit)
        actions.append(
            {
                "path": f"initial_guess.{field}",
                "from": getattr(initial, field),
                "to": getattr(updated_initial, field),
                "bounds": [lower, upper],
                "trigger_constraint_ids": sorted(action_triggers[field]),
                "reason": " ".join(dict.fromkeys(action_reasons[field])),
            }
        )
    if next_max_iterations != request.max_iterations:
        actions.append(
            {
                "path": "solver.max_iterations",
                "from": request.max_iterations,
                "to": next_max_iterations,
                "bounds": [1, 500],
                "trigger_constraint_ids": ["class1.weight_closure"],
                "reason": "Allow the restarted fixed-point loop additional bounded iterations.",
            }
        )

    record = {
        "repair_attempt": repair_attempt,
        "strategy": "bounded_design_variables_only",
        "requirements_changed": False,
        "trigger_constraint_ids": failed_ids,
        "actions": actions,
    }
    provenance = copy.deepcopy(request.provenance)
    history = provenance.get("auto_repair_history")
    if not isinstance(history, list):
        history = []
    provenance["auto_repair_history"] = [*history, copy.deepcopy(record)]
    repaired = replace(
        request,
        initial_guess=updated_initial,
        max_iterations=next_max_iterations,
        provenance=provenance,
    )
    return AircraftDesignRepairProposal(request=repaired, record=record)
