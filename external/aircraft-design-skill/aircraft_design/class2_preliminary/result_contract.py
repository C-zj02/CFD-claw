from __future__ import annotations

from typing import Any

from .constraints import normalized_constraint


SCHEMA_ID = "aircraft-design/design-data"
SCHEMA_VERSION = 2


def stage_record(
    status: str,
    *,
    blocking: bool,
    message: str,
    error: str | None = None,
) -> dict[str, Any]:
    if status not in {"completed", "partial", "failed", "skipped", "not_converged"}:
        raise ValueError(f"Unsupported stage status: {status}")
    record: dict[str, Any] = {"status": status, "blocking": blocking, "message": message}
    if error:
        record["error"] = error
    return record


def blocking_constraints_passed(constraints: list[dict]) -> bool:
    blocking = [item for item in constraints if item.get("blocking") is True]
    return bool(blocking) and all(item.get("passed") is True for item in blocking)


def engineering_feasible(
    *,
    numerical_converged: bool,
    constraints: list[dict],
    stage_status: dict[str, dict],
) -> bool:
    if not numerical_converged or not blocking_constraints_passed(constraints):
        return False
    for stage in stage_status.values():
        if stage.get("blocking") is True and stage.get("status") != "completed":
            return False
    return True


def normalized_advanced_constraints(
    advanced_results: dict,
    *,
    available_fuel_kg: float,
    class1_structure_kg: float,
) -> list[dict]:
    constraints: list[dict] = []
    propulsion = advanced_results.get("stage3_propulsion")
    if isinstance(propulsion, dict) and propulsion:
        for phase, label in (("cruise", "Cruise thrust margin"), ("climb", "Climb thrust margin")):
            constraints.append(
                normalized_constraint(
                    constraint_id=f"advanced.propulsion.{phase}_thrust_margin",
                    label=label,
                    category="propulsion",
                    direction="minimum",
                    required=0.0,
                    actual=propulsion.get(f"thrust_margin_{phase}"),
                    unit="ratio",
                    blocking=True,
                    evidence={"model": "Altitude- and speed-lapsed installed thrust", "prediction": True},
                    recommendation=f"Increase installed thrust or reduce the {phase} thrust requirement.",
                )
            )

    mission = advanced_results.get("stage4_mission")
    if isinstance(mission, dict) and mission:
        constraints.append(
            normalized_constraint(
                constraint_id="advanced.mission.fuel_capacity",
                label="Available mission fuel",
                category="mission",
                direction="minimum",
                required=float(mission.get("total_fuel_kg", 0.0)),
                actual=available_fuel_kg,
                unit="kg",
                blocking=True,
                evidence={"model": "Segment mission fuel analysis", "prediction": True},
                recommendation="Reduce mission demand or close the weight loop with the advanced mission fuel requirement.",
            )
        )

    stability = advanced_results.get("stage5_stability")
    if isinstance(stability, dict) and stability:
        constraints.extend(
            [
                normalized_constraint(
                    constraint_id="advanced.stability.static_margin_min",
                    label="Minimum static margin",
                    category="stability",
                    direction="minimum",
                    required=0.05,
                    actual=stability.get("static_margin"),
                    unit="cbar",
                    blocking=True,
                    evidence={"model": "Neutral-point and trim estimate", "prediction": True},
                    recommendation="Move the CG forward or increase horizontal-tail effectiveness.",
                ),
                normalized_constraint(
                    constraint_id="advanced.stability.static_margin_max",
                    label="Maximum recommended static margin",
                    category="stability",
                    direction="maximum",
                    required=0.25,
                    actual=stability.get("static_margin"),
                    unit="cbar",
                    blocking=False,
                    evidence={"model": "Handling-quality screening band", "prediction": True},
                    recommendation="Review control authority if the aircraft is excessively stable.",
                ),
            ]
        )

    structures = advanced_results.get("stage6_structures")
    if isinstance(structures, dict) and structures and class1_structure_kg > 0.0:
        constraints.append(
            normalized_constraint(
                constraint_id="advanced.structures.weight_feedback",
                label="Advanced structural-weight feedback",
                category="structures",
                direction="maximum",
                required=class1_structure_kg,
                actual=structures.get("structural_weight_kg"),
                unit="kg",
                blocking=True,
                evidence={"model": "Wing-root load and wingbox sizing feedback", "prediction": True},
                recommendation="Feed the advanced structural estimate back into MTOW sizing and rerun closure.",
            )
        )

    geometry_constraints = advanced_results.get("geometry_constraints", [])
    if isinstance(geometry_constraints, list):
        for index, item in enumerate(geometry_constraints):
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", f"geometry_{index}"))
            if name == "Fuel Volume":
                direction = "minimum"
            elif name == "Aspect Ratio Limit":
                direction = "maximum"
            else:
                # Unknown legacy geometry checks already expose a positive-pass
                # margin, but their physical direction is not safe to guess.
                direction = "minimum"
            constraint = normalized_constraint(
                constraint_id=f"advanced.geometry.{name.lower().replace(' ', '_')}",
                label=name,
                category="geometry",
                direction=direction,
                required=float(item.get("limit_value", 0.0)),
                actual=item.get("actual_value"),
                unit="m3" if name == "Fuel Volume" else "ratio",
                blocking=True,
                evidence={"model": item.get("description", "Geometry constraint check"), "prediction": True},
                recommendation=(
                    "Increase usable wing tank volume or reduce mission fuel."
                    if name == "Fuel Volume"
                    else "Revise the geometry to satisfy the stated limit."
                ),
            )
            constraints.append(constraint)

    optimization = advanced_results.get("stage7_optimization")
    if isinstance(optimization, dict) and optimization:
        # ``feasible_designs`` is retained as a legacy field name.  Stage 7
        # currently applies a reduced-order screening model, not the complete
        # multidisciplinary stage-gate workflow.
        feasible_count = len(optimization.get("feasible_designs", []))
        constraints.append(
            normalized_constraint(
                constraint_id="advanced.optimization.reduced_order_screened_candidates",
                label="Reduced-order screened candidates",
                category="optimization",
                direction="minimum",
                required=1.0,
                actual=float(feasible_count),
                unit="count",
                blocking=False,
                evidence={
                    "model": "Seeded reduced-order engineering screening; full stage-gate revalidation not performed",
                    "prediction": True,
                    "seed": optimization.get("exploration_seed", 0),
                    "evaluation_scope": optimization.get("evaluation_scope", "reduced_order_screening"),
                    "engineering_revalidation_performed": bool(
                        optimization.get("engineering_revalidation_performed", False)
                    ),
                },
                recommendation=(
                    "Re-run promising screened candidates through the complete engineering stage gates "
                    "before comparison or design freeze."
                ),
            )
        )

    return constraints
