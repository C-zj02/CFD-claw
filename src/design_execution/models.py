"""Structured contracts for deterministic aircraft design execution."""

from __future__ import annotations

import copy
import math
import re
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class DesignRunStage(str, Enum):
    PREPARING = "preparing"
    RUNNING = "running"
    VALIDATING = "validating"
    COMPLETED = "completed"
    NONCONVERGED = "nonconverged"
    ENGINEERING_INFEASIBLE = "engineering_infeasible"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"


class DesignRunStatus(str, Enum):
    COMPLETED = "completed"
    NONCONVERGED = "nonconverged"
    ENGINEERING_INFEASIBLE = "engineering_infeasible"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"


@dataclass(frozen=True)
class DesignValidationIssue:
    code: str
    message: str
    severity: str = "error"

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class AircraftDesignEngineeringResult:
    """Normalized engineering evidence exposed by every deterministic run."""

    numerical_converged: bool | None
    engineering_feasible: bool | None
    overall_status: str
    constraints: list[dict[str, Any]] = field(default_factory=list)
    stage_status: dict[str, dict[str, Any]] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)
    requirement_comparisons: list[dict[str, Any]] = field(default_factory=list)
    iteration_history: list[dict[str, Any]] = field(default_factory=list)
    design_point: dict[str, Any] = field(default_factory=dict)
    recommendations: list[str] = field(default_factory=list)

    @property
    def blocking_failed_count(self) -> int:
        return sum(
            1
            for constraint in self.constraints
            if constraint.get("blocking") is True and constraint.get("passed") is False
        )

    def to_dict(self, *, compact: bool = False) -> dict[str, Any]:
        headline = {
            "numerical_converged": self.numerical_converged,
            "engineering_feasible": self.engineering_feasible,
            "overall_status": self.overall_status,
            "blocking_failed_count": self.blocking_failed_count,
        }
        if compact:
            return headline
        return {
            **headline,
            "constraints": copy.deepcopy(self.constraints),
            "stage_status": copy.deepcopy(self.stage_status),
            "provenance": copy.deepcopy(self.provenance),
            "requirement_comparisons": copy.deepcopy(self.requirement_comparisons),
            "iteration_history": copy.deepcopy(self.iteration_history),
            "design_point": copy.deepcopy(self.design_point),
            "recommendations": list(self.recommendations),
            "diagnostic_recommendations": list(self.recommendations),
        }


@dataclass(frozen=True)
class DesignRunEvent:
    stage: DesignRunStage
    message: str
    progress: int
    detail: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage.value,
            "message": self.message,
            "progress": self.progress,
            "detail": self.detail,
        }


def _number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError(f"{name} must be finite")
    return parsed


def _bounded(value: Any, name: str, minimum: float, maximum: float) -> float:
    parsed = _number(value, name)
    if parsed < minimum or parsed > maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return parsed


@dataclass(frozen=True)
class AircraftDesignRequirements:
    range_m: float
    payload_kg: float
    cruise_mach: float = 0.22
    cruise_altitude_m: float = 6_000.0
    takeoff_distance_m: float = 1_000.0
    landing_distance_m: float = 1_000.0
    max_load_factor: float = 3.8
    sustained_turn_g: float = 2.0
    service_ceiling_m: float = 8_000.0
    aircraft_role: str = "uav"
    propulsion_type: str = "prop"
    reserve_fraction: float = 0.05
    tail_layout: str = "conventional"
    cl_max_takeoff: float = 1.8
    cl_max_landing: float = 2.0
    assumed_climb_rate_m_s: float = 5.0
    uncertainty_enabled: bool = False

    def __post_init__(self) -> None:
        values = {
            "range_m": _bounded(self.range_m, "requirements.range_m", 1_000.0, 30_000_000.0),
            "payload_kg": _bounded(self.payload_kg, "requirements.payload_kg", 0.0, 500_000.0),
            "cruise_mach": _bounded(self.cruise_mach, "requirements.cruise_mach", 0.03, 5.0),
            "cruise_altitude_m": _bounded(
                self.cruise_altitude_m, "requirements.cruise_altitude_m", 0.0, 35_000.0
            ),
            "takeoff_distance_m": _bounded(
                self.takeoff_distance_m, "requirements.takeoff_distance_m", 20.0, 10_000.0
            ),
            "landing_distance_m": _bounded(
                self.landing_distance_m, "requirements.landing_distance_m", 20.0, 10_000.0
            ),
            "max_load_factor": _bounded(
                self.max_load_factor, "requirements.max_load_factor", 1.0, 15.0
            ),
            "sustained_turn_g": _bounded(
                self.sustained_turn_g, "requirements.sustained_turn_g", 0.0, 10.0
            ),
            "service_ceiling_m": _bounded(
                self.service_ceiling_m, "requirements.service_ceiling_m", 100.0, 40_000.0
            ),
            "reserve_fraction": _bounded(
                self.reserve_fraction, "requirements.reserve_fraction", 0.0, 1.0
            ),
            "cl_max_takeoff": _bounded(
                self.cl_max_takeoff, "requirements.cl_max_takeoff", 0.1, 8.0
            ),
            "cl_max_landing": _bounded(
                self.cl_max_landing, "requirements.cl_max_landing", 0.1, 8.0
            ),
            "assumed_climb_rate_m_s": _bounded(
                self.assumed_climb_rate_m_s,
                "requirements.assumed_climb_rate_m_s",
                0.1,
                300.0,
            ),
        }
        if values["service_ceiling_m"] < values["cruise_altitude_m"]:
            raise ValueError("requirements.service_ceiling_m must not be below cruise_altitude_m")
        if values["reserve_fraction"] >= 1.0:
            raise ValueError("requirements.reserve_fraction must be less than 1.0")
        for name, value in values.items():
            object.__setattr__(self, name, value)
        if not isinstance(self.aircraft_role, str):
            raise ValueError("requirements.aircraft_role must be a string")
        aircraft_role = self.aircraft_role.strip().lower().replace(" ", "_")
        if not aircraft_role or len(aircraft_role) > 60:
            raise ValueError("requirements.aircraft_role must be a non-empty label up to 60 characters")
        if not isinstance(self.propulsion_type, str):
            raise ValueError("requirements.propulsion_type must be a string")
        propulsion_type = self.propulsion_type.strip().lower()
        if propulsion_type not in {"jet", "prop"}:
            raise ValueError("requirements.propulsion_type must be jet or prop")
        if not isinstance(self.tail_layout, str):
            raise ValueError("requirements.tail_layout must be a string")
        tail_layout = self.tail_layout.strip().lower()
        if tail_layout not in {"conventional", "t_tail", "v_tail", "twin_fin"}:
            raise ValueError(
                "requirements.tail_layout must be conventional, t_tail, v_tail, or twin_fin"
            )
        if not isinstance(self.uncertainty_enabled, bool):
            raise ValueError("requirements.uncertainty_enabled must be a boolean")
        object.__setattr__(self, "aircraft_role", aircraft_role)
        object.__setattr__(self, "propulsion_type", propulsion_type)
        object.__setattr__(self, "tail_layout", tail_layout)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "AircraftDesignRequirements":
        if not isinstance(value, dict):
            raise ValueError("requirements must be an object")
        allowed = set(cls.__dataclass_fields__)
        unknown = sorted(set(value) - allowed)
        if unknown:
            raise ValueError(f"unsupported requirement fields: {', '.join(unknown)}")
        missing = [name for name in ("range_m", "payload_kg") if name not in value]
        if missing:
            raise ValueError(f"missing requirement fields: {', '.join(missing)}")
        return cls(**value)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AircraftDesignInitialGuess:
    mtow_kg: float
    wing_loading_pa: float = 3_000.0
    thrust_to_weight: float = 0.6
    aspect_ratio: float = 10.0
    sweep_deg: float = 5.0
    taper_ratio: float = 0.5
    thickness_ratio: float = 0.12
    # Canonical propulsion-energy inputs. ``sfc_cruise_1_s`` is retained only
    # for legacy requests and is migrated at the declared cruise condition.
    sfc_cruise_1_s: float | None = None
    jet_tsfc_kg_per_n_s: float | None = None
    prop_bsfc_kg_per_j: float | None = None
    prop_efficiency: float = 0.8
    cd0: float = 0.025
    oswald_e: float = 0.82

    def __post_init__(self) -> None:
        values = {
            "mtow_kg": _bounded(self.mtow_kg, "initial_guess.mtow_kg", 1.0, 2_000_000.0),
            "wing_loading_pa": _bounded(
                self.wing_loading_pa, "initial_guess.wing_loading_pa", 50.0, 20_000.0
            ),
            "thrust_to_weight": _bounded(
                self.thrust_to_weight, "initial_guess.thrust_to_weight", 0.02, 3.0
            ),
            "aspect_ratio": _bounded(self.aspect_ratio, "initial_guess.aspect_ratio", 1.0, 40.0),
            "sweep_deg": _bounded(self.sweep_deg, "initial_guess.sweep_deg", 0.0, 75.0),
            "taper_ratio": _bounded(self.taper_ratio, "initial_guess.taper_ratio", 0.05, 1.0),
            "thickness_ratio": _bounded(
                self.thickness_ratio, "initial_guess.thickness_ratio", 0.03, 0.3
            ),
            "prop_efficiency": _bounded(
                self.prop_efficiency, "initial_guess.prop_efficiency", 0.1, 1.0
            ),
            "cd0": _bounded(self.cd0, "initial_guess.cd0", 0.001, 0.3),
            "oswald_e": _bounded(self.oswald_e, "initial_guess.oswald_e", 0.1, 1.2),
        }
        for name, value in values.items():
            object.__setattr__(self, name, value)
        optional_values = {
            "sfc_cruise_1_s": (self.sfc_cruise_1_s, 1e-10, 0.01),
            "jet_tsfc_kg_per_n_s": (self.jet_tsfc_kg_per_n_s, 1e-9, 0.001),
            "prop_bsfc_kg_per_j": (self.prop_bsfc_kg_per_j, 1e-10, 1e-5),
        }
        for name, (value, minimum, maximum) in optional_values.items():
            if value is not None:
                object.__setattr__(self, name, _bounded(value, f"initial_guess.{name}", minimum, maximum))

    @classmethod
    def defaults_for(cls, requirements: AircraftDesignRequirements) -> "AircraftDesignInitialGuess":
        small = requirements.payload_kg < 50.0 and requirements.range_m < 500_000.0
        return cls(
            mtow_kg=max(25.0, requirements.payload_kg * 5.0),
            wing_loading_pa=350.0 if small else 3_000.0,
            thrust_to_weight=0.35 if small else 0.6,
            aspect_ratio=9.0 if small else 10.0,
            sweep_deg=0.0 if small else 5.0,
            sfc_cruise_1_s=None,
            jet_tsfc_kg_per_n_s=(2.3e-5 if requirements.propulsion_type == "jet" else None),
            prop_bsfc_kg_per_j=(8.45e-8 if requirements.propulsion_type == "prop" else None),
            prop_efficiency=0.8,
            cd0=0.032 if small else 0.025,
        )

    @classmethod
    def from_dict(
        cls,
        value: dict[str, Any],
        requirements: AircraftDesignRequirements,
    ) -> "AircraftDesignInitialGuess":
        if not isinstance(value, dict):
            raise ValueError("initial_guess must be an object")
        allowed = set(cls.__dataclass_fields__)
        unknown = sorted(set(value) - allowed)
        if unknown:
            raise ValueError(f"unsupported initial guess fields: {', '.join(unknown)}")
        defaults = cls.defaults_for(requirements).to_dict()
        legacy_value = value.get("sfc_cruise_1_s")
        canonical_field = (
            "jet_tsfc_kg_per_n_s"
            if requirements.propulsion_type == "jet"
            else "prop_bsfc_kg_per_j"
        )
        if legacy_value is not None and canonical_field not in value:
            # An explicit legacy value must be migrated upstream rather than
            # silently losing to the new canonical default.
            defaults[canonical_field] = None
        defaults.update(value)
        return cls(**defaults)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AircraftDesignRequest:
    project_name: str
    requirements: AircraftDesignRequirements
    initial_guess: AircraftDesignInitialGuess
    tolerance: float = 0.001
    max_iterations: int = 50
    provenance: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", self.project_name.strip()).strip("_")
        if not cleaned:
            raise ValueError("project_name must contain letters or numbers")
        if len(cleaned) > 80:
            raise ValueError("project_name must be at most 80 characters")
        object.__setattr__(self, "project_name", cleaned)
        object.__setattr__(self, "tolerance", _bounded(self.tolerance, "tolerance", 1e-6, 0.1))
        if isinstance(self.max_iterations, bool) or not isinstance(self.max_iterations, int):
            raise ValueError("max_iterations must be an integer")
        if self.max_iterations < 1 or self.max_iterations > 500:
            raise ValueError("max_iterations must be between 1 and 500")
        if not isinstance(self.provenance, dict):
            raise ValueError("provenance must be an object")
        object.__setattr__(self, "provenance", copy.deepcopy(self.provenance))

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "AircraftDesignRequest":
        if not isinstance(value, dict):
            raise ValueError("design request must be an object")
        allowed = {
            "project_name",
            "requirements",
            "initial_guess",
            "tolerance",
            "max_iterations",
            "solver_options",
            "provenance",
        }
        unknown = sorted(set(value) - allowed)
        if unknown:
            raise ValueError(f"unsupported design request fields: {', '.join(unknown)}")
        solver_options = value.get("solver_options", {})
        if not isinstance(solver_options, dict):
            raise ValueError("solver_options must be an object")
        unknown_solver_options = sorted(
            set(solver_options) - {"tolerance", "max_iter", "max_iterations"}
        )
        if unknown_solver_options:
            raise ValueError(
                f"unsupported solver option fields: {', '.join(unknown_solver_options)}"
            )
        requirements_value = value.get("requirements")
        requirements = AircraftDesignRequirements.from_dict(requirements_value)
        initial_value = value.get("initial_guess", {})
        initial_guess = AircraftDesignInitialGuess.from_dict(initial_value, requirements)
        tolerance = value.get("tolerance", solver_options.get("tolerance", 0.001))
        max_iterations = value.get(
            "max_iterations",
            solver_options.get("max_iterations", solver_options.get("max_iter", 50)),
        )
        provenance = value.get("provenance")
        if provenance is None:
            requirement_user_fields = set(requirements_value)
            initial_user_fields = set(initial_value)
            canonical_energy_field = (
                "jet_tsfc_kg_per_n_s"
                if requirements.propulsion_type == "jet"
                else "prop_bsfc_kg_per_j"
            )
            legacy_energy_provided = initial_value.get("sfc_cruise_1_s") is not None
            if canonical_energy_field in initial_user_fields:
                energy_source = "user"
            elif legacy_energy_provided:
                energy_source = "legacy_migrated_at_cruise_condition"
            else:
                energy_source = "default"
            provenance = {
                "request_contract_version": 2,
                "propulsion_energy": {
                    "propulsion_type": requirements.propulsion_type,
                    "canonical_field": canonical_energy_field,
                    "source": energy_source,
                    "legacy_field": (
                        "sfc_cruise_1_s" if legacy_energy_provided else None
                    ),
                    "legacy_semantics": (
                        "equivalent fuel-weight-flow / thrust at the declared cruise condition [1/s]"
                        if legacy_energy_provided
                        else None
                    ),
                },
                "input_fields": {
                    "requirements": {
                        name: {
                            "source": "user" if name in requirement_user_fields else "default",
                            "value": copy.deepcopy(field_value),
                        }
                        for name, field_value in requirements.to_dict().items()
                    },
                    "initial_guess": {
                        name: {
                            "source": "user" if name in initial_user_fields else "derived",
                            "value": copy.deepcopy(field_value),
                        }
                        for name, field_value in initial_guess.to_dict().items()
                    },
                },
            }
        elif not isinstance(provenance, dict):
            raise ValueError("provenance must be an object")
        return cls(
            project_name=str(value.get("project_name") or "aircraft_design"),
            requirements=requirements,
            initial_guess=initial_guess,
            tolerance=tolerance,
            max_iterations=max_iterations,
            provenance=provenance,
        )

    def to_upstream_dict(self) -> dict[str, Any]:
        return {
            "requirements": self.requirements.to_dict(),
            "initial_guess": self.initial_guess.to_dict(),
            "solver_options": {
                "tolerance": self.tolerance,
                "max_iter": self.max_iterations,
            },
            "provenance": copy.deepcopy(self.provenance),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_name": self.project_name,
            "requirements": self.requirements.to_dict(),
            "initial_guess": self.initial_guess.to_dict(),
            "tolerance": self.tolerance,
            "max_iterations": self.max_iterations,
            "provenance": copy.deepcopy(self.provenance),
        }
