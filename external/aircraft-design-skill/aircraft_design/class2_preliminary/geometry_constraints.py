from dataclasses import dataclass, field
import math
from typing import List, Dict
from ..class3_detailed.geometry_detailed import DetailedFuselage, DetailedWing, estimate_wing_fuel_volume


@dataclass
class GeometricConstraint:
    name: str
    description: str
    passed: bool
    actual_value: float
    limit_value: float
    margin: float
    details: dict = field(default_factory=dict)


FUSELAGE_TANK_ENVELOPE_FRACTIONS = {
    "uav": 0.15,
    "fighter": 0.12,
    "light_fighter": 0.12,
    "trainer": 0.08,
    "general_aviation": 0.08,
    "business_jet": 0.05,
    "transport": 0.04,
}


def estimate_usable_fuel_volume(
    *,
    wing_area_m2: float,
    wing_span_m: float,
    thickness_ratio: float,
    taper_ratio: float,
    fuselage_length_m: float,
    fuselage_diameter_m: float,
    aircraft_role: str,
    fuselage_tank_fraction: float | None = None,
) -> dict:
    """Estimate auditable wing plus center/fuselage usable tank volume."""

    wing_volume_m3 = estimate_wing_fuel_volume(
        area_m2=wing_area_m2,
        span_m=wing_span_m,
        t_c_root=thickness_ratio,
        t_c_tip=thickness_ratio,
        taper=taper_ratio,
    )
    role = str(aircraft_role or "").strip().lower()
    default_fraction = FUSELAGE_TANK_ENVELOPE_FRACTIONS.get(role, 0.06)
    fraction = default_fraction if fuselage_tank_fraction is None else float(fuselage_tank_fraction)
    fraction = min(0.30, max(0.0, fraction))
    fuselage_envelope_m3 = math.pi * (max(0.0, fuselage_diameter_m) / 2.0) ** 2 * max(
        0.0, fuselage_length_m
    )
    fuselage_tank_volume_m3 = fuselage_envelope_m3 * fraction
    return {
        "total_m3": wing_volume_m3 + fuselage_tank_volume_m3,
        "wing_m3": wing_volume_m3,
        "fuselage_or_center_tank_m3": fuselage_tank_volume_m3,
        "fuselage_envelope_fraction": fraction,
        "aircraft_role": role or "unspecified",
    }


class GeometryConstraintChecker:
    def __init__(self, wing: DetailedWing, fuselage: DetailedFuselage, requirements: Dict[str, float]):
        self.wing = wing
        self.fuselage = fuselage
        self.reqs = requirements
        self.results: List[GeometricConstraint] = []

    def check_all(self) -> List[GeometricConstraint]:
        self.check_fuel_volume()
        self.check_aspect_ratio()
        self.check_landing_gear_clearance()
        return self.results

    def check_fuel_volume(self):
        # Calculate available volume
        # Simple estimate: Wing volume * 0.7 (tank efficiency) * 0.85 (wet wing ratio)
        # Using imported estimator if available, else simple geometric
        # Assuming estimate_wing_fuel_volume returns m3
        volume = estimate_usable_fuel_volume(
            wing_area_m2=self.wing.area,
            wing_span_m=self.wing.span,
            thickness_ratio=self.wing.thickness_to_chord_root,
            taper_ratio=self.wing.taper_ratio,
            fuselage_length_m=self.fuselage.length,
            fuselage_diameter_m=self.fuselage.diameter,
            aircraft_role=str(self.reqs.get("aircraft_role", "")),
            fuselage_tank_fraction=self.reqs.get("fuselage_tank_fraction"),
        )
        vol_m3 = volume["total_m3"]
        req_fuel_kg = self.reqs.get("fuel_weight_kg", 0.0)
        fuel_density = 800.0  # kg/m3 (Jet A)
        req_vol_m3 = req_fuel_kg / fuel_density

        passed = vol_m3 >= req_vol_m3
        self.results.append(
            GeometricConstraint(
                name="Fuel Volume",
                description="Usable wing plus center/fuselage tank volume vs required fuel volume",
                passed=passed,
                actual_value=vol_m3,
                limit_value=req_vol_m3,
                margin=vol_m3 - req_vol_m3,
                details=volume,
            )
        )

    def check_aspect_ratio(self):
        # Limit AR to avoid structural issues or gate limits (indirectly)
        # Example limit AR < 12 for standard cantilever
        limit = self.reqs.get("max_aspect_ratio", 14.0)
        ar = self.wing.span**2 / self.wing.area
        passed = ar <= limit
        self.results.append(
            GeometricConstraint(
                name="Aspect Ratio Limit",
                description=f"Aspect Ratio <= {limit}",
                passed=passed,
                actual_value=ar,
                limit_value=limit,
                margin=limit - ar,
            )
        )

    def check_landing_gear_clearance(self):
        # Example: Fuselage diameter vs upsweep for takeoff rotation
        # Simplified check
        pass
