"""Projection between versioned design intent and the deterministic solver.

The declared intent is always the source of truth. The solver request is a
strict projection and keeps unsupported or soft fields in provenance so that
they cannot disappear from reports or audits.
"""

from __future__ import annotations

import copy
from dataclasses import replace
from typing import Any, Mapping

from src.design_execution.models import (
    AircraftDesignInitialGuess,
    AircraftDesignRequest,
    AircraftDesignRequirements,
)

from .models import (
    DesignIntent,
    DesignIntentStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)


_TECHNOLOGY_REQUIREMENTS = {
    "cl_max_takeoff",
    "cl_max_landing",
    "assumed_climb_rate_m_s",
    "uncertainty_enabled",
}

_CONFIGURATION_REQUIREMENTS = {
    "aircraft_role",
    "propulsion_type",
    "tail_layout",
}

_TECHNOLOGY_INITIAL_FIELDS = {
    "sfc_cruise_1_s",
    "jet_tsfc_kg_per_n_s",
    "prop_bsfc_kg_per_j",
    "prop_efficiency",
    "cd0",
    "oswald_e",
}

_DECLARED_PATHS = {
    "max_mtow_kg": "weights.max_mtow_kg",
    "max_aspect_ratio": "geometry.max_aspect_ratio",
    "min_cruise_endurance_s": "performance.min_cruise_endurance_s",
    "max_flight_mach": "performance.max_flight_mach",
    "launch_mode": "launch.mode",
    "launch_field_altitude_m": "launch.field_altitude_m",
    "booster_end_mach": "launch.booster_end_mach",
    "booster_end_relative_altitude_m": "launch.booster_end_relative_altitude_m",
    "recovery_mode": "recovery.mode",
    "parachute_open_mach": "recovery.parachute_open_mach",
    "parachute_open_relative_altitude_m": "recovery.parachute_open_relative_altitude_m",
    "engine_count": "propulsion.engine_count",
    "configuration_reference": "configuration.reference",
    "stealth_requirement": "configuration.stealth_requirement",
}

_PATH_TO_DECLARED = {path: name for name, path in _DECLARED_PATHS.items()}


def _source(value: Any) -> RequirementSource:
    normalized = str(value or "default").strip().lower()
    if normalized == "user":
        return RequirementSource.USER
    if normalized == "reference":
        return RequirementSource.REFERENCE
    if normalized == "default":
        return RequirementSource.DEFAULT
    return RequirementSource.DERIVED


def _field_source(
    provenance: Mapping[str, Any],
    group: str,
    name: str,
    *,
    fallback: RequirementSource,
) -> RequirementSource:
    input_fields = provenance.get("input_fields")
    group_fields = input_fields.get(group) if isinstance(input_fields, Mapping) else None
    entry = group_fields.get(name) if isinstance(group_fields, Mapping) else None
    value = entry.get("source") if isinstance(entry, Mapping) else None
    return _source(value) if value is not None else fallback


def _unit_for(path: str) -> str | None:
    leaf = path.rsplit(".", 1)[-1]
    if leaf.endswith("_kg"):
        return "kg"
    if leaf.endswith("_m"):
        return "m"
    if leaf.endswith("_s"):
        return "s"
    if leaf.endswith("_pa"):
        return "Pa"
    if "mach" in leaf:
        return "Mach"
    if leaf == "engine_count":
        return "count"
    return None


def intent_from_aircraft_request(
    request: AircraftDesignRequest,
    *,
    intent_id: str | None = None,
    original_request: str | None = None,
    field_sources: Mapping[str, str] | None = None,
) -> DesignIntent:
    """Represent an existing strict solver request as a versioned intent."""

    if not isinstance(request, AircraftDesignRequest):
        raise ValueError("request must be an AircraftDesignRequest")
    provenance = request.provenance
    fields: dict[str, RequirementField] = {}

    for name, value in request.requirements.to_dict().items():
        source_path = f"requirements.{name}"
        source = (
            _source(field_sources[source_path])
            if field_sources is not None and source_path in field_sources
            else _field_source(
                provenance,
                "requirements",
                name,
                fallback=RequirementSource.DEFAULT,
            )
        )
        if name in _TECHNOLOGY_REQUIREMENTS:
            role = RequirementRole.TECHNOLOGY_ASSUMPTION
        elif name in _CONFIGURATION_REQUIREMENTS and source is not RequirementSource.USER:
            role = RequirementRole.DESIGN_VARIABLE
        elif source is RequirementSource.USER:
            role = RequirementRole.HARD_CONSTRAINT
        else:
            role = RequirementRole.TECHNOLOGY_ASSUMPTION
        path = source_path
        fields[path] = RequirementField(
            path=path,
            value=value,
            unit=_unit_for(path),
            role=role,
            locked=role is RequirementRole.HARD_CONSTRAINT,
            source=source,
            confidence=1.0 if source is RequirementSource.USER else 0.8,
        )

    for name, value in request.initial_guess.to_dict().items():
        if value is None:
            continue
        path = f"initial_guess.{name}"
        source = (
            _source(field_sources[path])
            if field_sources is not None and path in field_sources
            else _field_source(
                provenance,
                "initial_guess",
                name,
                fallback=RequirementSource.DERIVED,
            )
        )
        fields[path] = RequirementField(
            path=path,
            value=value,
            unit=_unit_for(path),
            role=(
                RequirementRole.TECHNOLOGY_ASSUMPTION
                if name in _TECHNOLOGY_INITIAL_FIELDS
                else RequirementRole.DESIGN_VARIABLE
            ),
            locked=False,
            source=source,
            confidence=1.0 if source is RequirementSource.USER else 0.75,
        )

    declared = provenance.get("user_requirements")
    if not isinstance(declared, Mapping):
        nested = provenance.get("user_provenance")
        declared = nested.get("user_requirements") if isinstance(nested, Mapping) else None
    if isinstance(declared, Mapping):
        for name, value in declared.items():
            path = _DECLARED_PATHS.get(str(name))
            if path is None or path in fields:
                continue
            soft = name == "configuration_reference"
            fields[path] = RequirementField(
                path=path,
                value=copy.deepcopy(value),
                unit=_unit_for(path),
                role=RequirementRole.SOFT_GOAL if soft else RequirementRole.HARD_CONSTRAINT,
                locked=not soft,
                source=RequirementSource.USER,
            )

    resolved_id = intent_id or f"solver-request-{request.project_name}"
    return DesignIntent(
        intent_id=resolved_id,
        requirements=tuple(fields.values()),
        status=DesignIntentStatus.NEEDS_CLARIFICATION,
        original_request=original_request,
        aircraft_class=request.requirements.aircraft_role,
        configuration=request.requirements.tail_layout,
        propulsion=request.requirements.propulsion_type,
        metadata={
            "projection": {"source": "aircraft_design_request", "contract_version": 1},
            "project_name": request.project_name,
        },
    )


def solver_request_from_intent(
    intent: DesignIntent,
    *,
    project_name: str | None = None,
    require_ready: bool = True,
) -> AircraftDesignRequest:
    """Build a strict solver request while retaining the complete intent.

    This function never declares a request ready. Callers must diagnose and
    confirm the intent first; ``require_ready=False`` exists for preflight and
    test projection only and must not be used to submit a job.
    """

    if not isinstance(intent, DesignIntent):
        raise ValueError("intent must be a DesignIntent")
    if require_ready and intent.status is not DesignIntentStatus.READY_FOR_SOLVER:
        raise ValueError("design intent must be ready_for_solver before projection")

    requirement_fields = set(AircraftDesignRequirements.__dataclass_fields__)
    initial_fields = set(AircraftDesignInitialGuess.__dataclass_fields__)
    requirements: dict[str, Any] = {}
    initial_guess: dict[str, Any] = {}
    user_requirements: dict[str, Any] = {}
    soft_goals: dict[str, Any] = {}
    field_provenance: dict[str, dict[str, dict[str, Any]]] = {
        "requirements": {},
        "initial_guess": {},
    }

    for field in intent.requirements:
        if field.path.startswith("requirements."):
            name = field.path.removeprefix("requirements.")
            if name in requirement_fields:
                requirements[name] = copy.deepcopy(field.value)
                field_provenance["requirements"][name] = {
                    "source": field.source.value,
                    "value": copy.deepcopy(field.value),
                    "role": field.role.value,
                    "locked": field.locked,
                }
                continue
        if field.path.startswith("initial_guess."):
            name = field.path.removeprefix("initial_guess.")
            if name in initial_fields:
                initial_guess[name] = copy.deepcopy(field.value)
                field_provenance["initial_guess"][name] = {
                    "source": field.source.value,
                    "value": copy.deepcopy(field.value),
                    "role": field.role.value,
                    "locked": field.locked,
                }
                continue
        declared_name = _PATH_TO_DECLARED.get(field.path)
        if declared_name is not None:
            destination = soft_goals if field.role is RequirementRole.SOFT_GOAL else user_requirements
            destination[declared_name] = copy.deepcopy(field.value)
        elif field.role is RequirementRole.SOFT_GOAL:
            # Keep deferred or extension fields directly addressable by
            # reporting code even when the strict solver has no native input
            # slot for them. The complete intent remains the authoritative
            # representation in all cases.
            soft_goals[field.path] = copy.deepcopy(field.value)

    missing = [name for name in ("range_m", "payload_kg") if name not in requirements]
    if missing:
        raise ValueError(f"design intent is missing solver requirements: {', '.join(missing)}")

    normalized_requirements = AircraftDesignRequirements.from_dict(requirements)
    defaults = AircraftDesignInitialGuess.defaults_for(normalized_requirements).to_dict()
    defaults.update(initial_guess)
    max_mtow = user_requirements.get("max_mtow_kg")
    if "mtow_kg" not in initial_guess and isinstance(max_mtow, (int, float)):
        defaults["mtow_kg"] = float(max_mtow)
    max_aspect_ratio = user_requirements.get("max_aspect_ratio")
    if "aspect_ratio" not in initial_guess and isinstance(max_aspect_ratio, (int, float)):
        defaults["aspect_ratio"] = min(defaults["aspect_ratio"], float(max_aspect_ratio))

    resolved_project = project_name or str(intent.metadata.get("project_name") or intent.intent_id)
    provenance = {
        "request_contract_version": 3,
        "requirement_intent": intent.to_dict(),
        "user_requirements": user_requirements,
        "soft_goals": soft_goals,
        "input_fields": field_provenance,
        "projection": {
            "contract_version": 1,
            "intent_id": intent.intent_id,
            "intent_revision": intent.revision,
            "complete_declared_intent_preserved": True,
        },
    }
    return AircraftDesignRequest.from_dict(
        {
            "project_name": resolved_project,
            "requirements": normalized_requirements.to_dict(),
            "initial_guess": defaults,
            "provenance": provenance,
        }
    )


def complete_intent_with_solver_defaults(intent: DesignIntent) -> DesignIntent:
    """Materialize every solver default as an auditable intent field.

    Call this only after the raw intent has passed clarification checks. The
    original fields always win, so completion cannot overwrite user values.
    """

    if not isinstance(intent, DesignIntent):
        raise ValueError("intent must be a DesignIntent")
    request = solver_request_from_intent(intent, require_ready=False)
    projected = intent_from_aircraft_request(request)
    original_paths = {field.path for field in intent.requirements}
    added = tuple(field for field in projected.requirements if field.path not in original_paths)
    metadata = intent.to_dict()["metadata"]
    metadata["solver_completion"] = {
        "contract_version": 1,
        "added_field_paths": [field.path for field in added],
        "requires_confirmation": bool(added),
    }
    return replace(
        intent,
        requirements=(*intent.requirements, *added),
        metadata=metadata,
    )


__all__ = [
    "complete_intent_with_solver_defaults",
    "intent_from_aircraft_request",
    "solver_request_from_intent",
]
