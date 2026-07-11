from __future__ import annotations

import bisect
import math
from dataclasses import dataclass, replace

from ..common.atmosphere import isa_tropopause
from ..common.units import CONST


@dataclass(frozen=True)
class PropulsionModel:
    type: str
    thrust_sl_n: float | None = None
    power_sl_w: float | None = None
    jet_tsfc_kg_per_n_s: float | None = None
    prop_bsfc_kg_per_j: float | None = None
    prop_efficiency: float | None = None
    jet_lapse_exp: float = 0.7
    prop_power_lapse_exp: float = 1.0
    mct_to_mto_ratio: float = 1.0
    jet_mach_factor: float = 0.0  # T = T_sl * sigma^n * (1 + factor * M)
    jet_model_method: str = "simple"  # "simple" or "mattingly_low_bypass"
    bypass_ratio: float = 0.3
    mil_to_ab_sfc_ratio: float = 2.5  # Ratio of AB SFC to Mil SFC (SL)
    tsfc_ab_1_s: float | None = None  # Explicit AB SFC if provided
    thrust_map: dict | None = None  # { "mach": [...], "altitude": [...], "thrust": [[...]] }
    sfc_map: dict | None = None  # { "mach": [...], "altitude": [...], "sfc": [[...]] }
    energy_source: str = "default"
    legacy_sfc_cruise_1_s: float | None = None
    reference_speed_m_s: float | None = None

    @property
    def tsfc_1_s(self) -> float | None:
        """Compatibility alias for legacy propulsion dictionaries.

        The canonical value is mass TSFC in kg/(N*s), despite the historical
        alias suggesting a pure inverse-time quantity.
        """

        return self.jet_tsfc_kg_per_n_s

    @property
    def sfc_1_s(self) -> float | None:
        """Compatibility alias for propeller BSFC, canonically kg/J."""

        return self.prop_bsfc_kg_per_j


JET_TSFC_DEFAULT_KG_PER_N_S = 2.3e-5
PROP_BSFC_DEFAULT_KG_PER_J = 8.45e-8
PROP_EFFICIENCY_DEFAULT = 0.8


def _positive_float(value: object, field_name: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a positive finite number.")
    parsed = float(value)
    if not math.isfinite(parsed) or parsed <= 0.0:
        raise ValueError(f"{field_name} must be a positive finite number.")
    return parsed


def build_propulsion_model(
    propulsion_in: dict, *, mtow_kg: float | None = None, thrust_to_weight: float | None = None
) -> PropulsionModel:
    ptype = str(propulsion_in["type"]).strip().lower()
    if ptype not in {"jet", "prop"}:
        raise ValueError("propulsion.type must be 'jet' or 'prop'.")
    thrust_sl_n = propulsion_in.get("thrust_sl_n", None)
    power_sl_w = propulsion_in.get("power_sl_w", None)

    if thrust_sl_n is None and mtow_kg is not None and thrust_to_weight is not None:
        thrust_sl_n = thrust_to_weight * mtow_kg * CONST.g0_m_s2

    jet_lapse_exp = float(propulsion_in.get("jet_lapse_exp", 0.7))
    prop_power_lapse_exp = float(propulsion_in.get("prop_power_lapse_exp", 1.0))
    mct_ratio = float(propulsion_in.get("mct_to_mto_ratio", 1.0))
    jet_mach_factor = float(propulsion_in.get("jet_mach_factor", 0.0))

    jet_model_method = propulsion_in.get("jet_model_method", "simple")
    bypass_ratio = float(propulsion_in.get("bypass_ratio", 0.3))

    jet_tsfc = _positive_float(
        propulsion_in.get("jet_tsfc_kg_per_n_s", propulsion_in.get("tsfc_kg_per_n_s")),
        "propulsion.jet_tsfc_kg_per_n_s",
    )
    energy_source = "canonical_input" if jet_tsfc is not None else "default"
    if jet_tsfc is None:
        # ``tsfc_1_s`` is a historical propulsion-dictionary alias. Existing
        # callers used it as kg/(N*s), so preserve that behavior exactly.
        jet_tsfc = _positive_float(propulsion_in.get("tsfc_1_s"), "propulsion.tsfc_1_s")
        if jet_tsfc is not None:
            energy_source = "legacy_propulsion_alias"
    tsfc_ab_1_s = propulsion_in.get("tsfc_ab_1_s", None)

    # If explicit AB SFC provided, calculate/override ratio or just store it
    mil_to_ab_sfc_ratio = float(propulsion_in.get("mil_to_ab_sfc_ratio", 2.5))
    if jet_tsfc is not None and tsfc_ab_1_s is not None and jet_tsfc > 0:
        mil_to_ab_sfc_ratio = tsfc_ab_1_s / jet_tsfc

    prop_bsfc = _positive_float(
        propulsion_in.get("prop_bsfc_kg_per_j", propulsion_in.get("bsfc_kg_per_j")),
        "propulsion.prop_bsfc_kg_per_j",
    )
    if ptype == "prop" and prop_bsfc is not None:
        energy_source = "canonical_input"
    if prop_bsfc is None:
        # ``sfc_1_s`` historically carried propeller BSFC in kg/J.
        prop_bsfc = _positive_float(propulsion_in.get("sfc_1_s"), "propulsion.sfc_1_s")
        if ptype == "prop" and prop_bsfc is not None:
            energy_source = "legacy_propulsion_alias"
    eta_prop = _positive_float(propulsion_in.get("prop_efficiency"), "propulsion.prop_efficiency")
    if eta_prop is not None and eta_prop > 1.0:
        raise ValueError("propulsion.prop_efficiency must be <= 1.0.")
    legacy_cruise_sfc = _positive_float(
        propulsion_in.get("legacy_sfc_cruise_1_s"),
        "propulsion.legacy_sfc_cruise_1_s",
    )
    reference_speed = _positive_float(
        propulsion_in.get("reference_speed_m_s"),
        "propulsion.reference_speed_m_s",
    )

    thrust_map = propulsion_in.get("thrust_map", None)
    sfc_map = propulsion_in.get("sfc_map", None)

    # Defaults for robustness
    if ptype == "jet" and jet_tsfc is None and legacy_cruise_sfc is not None:
        # Legacy sizing SFC was weight fuel-flow / thrust in 1/s. Convert to
        # mass TSFC using c_T = c_weight / g0.
        jet_tsfc = legacy_cruise_sfc / CONST.g0_m_s2
        energy_source = "legacy_sfc_cruise_1_s_migrated"
    if ptype == "jet" and jet_tsfc is None and sfc_map is None:
        jet_tsfc = JET_TSFC_DEFAULT_KG_PER_N_S
        energy_source = "default"

    if ptype == "prop":
        if eta_prop is None:
            eta_prop = PROP_EFFICIENCY_DEFAULT
        if prop_bsfc is None and legacy_cruise_sfc is not None:
            if reference_speed is None:
                raise ValueError(
                    "reference_speed_m_s is required to migrate propeller "
                    "legacy_sfc_cruise_1_s."
                )
            # Match the historical jet-form Breguet exponent at the declared
            # cruise point: c_P = c_legacy * eta_p / (g0 * V).
            prop_bsfc = (
                legacy_cruise_sfc * eta_prop / (CONST.g0_m_s2 * reference_speed)
            )
            energy_source = "legacy_sfc_cruise_1_s_migrated"
        if prop_bsfc is None:
            prop_bsfc = PROP_BSFC_DEFAULT_KG_PER_J
            energy_source = "default"
    resolved_energy_source = propulsion_in.get("resolved_energy_source")
    if isinstance(resolved_energy_source, str) and resolved_energy_source.strip():
        energy_source = resolved_energy_source.strip()

    return PropulsionModel(
        type=ptype,
        thrust_sl_n=thrust_sl_n,
        power_sl_w=power_sl_w,
        jet_tsfc_kg_per_n_s=jet_tsfc if ptype == "jet" else None,
        prop_bsfc_kg_per_j=prop_bsfc if ptype == "prop" else None,
        prop_efficiency=eta_prop,
        jet_lapse_exp=jet_lapse_exp,
        prop_power_lapse_exp=prop_power_lapse_exp,
        mct_to_mto_ratio=mct_ratio,
        jet_mach_factor=jet_mach_factor,
        jet_model_method=jet_model_method,
        bypass_ratio=bypass_ratio,
        mil_to_ab_sfc_ratio=mil_to_ab_sfc_ratio,
        tsfc_ab_1_s=tsfc_ab_1_s,
        thrust_map=thrust_map,
        sfc_map=sfc_map,
        energy_source=energy_source,
        legacy_sfc_cruise_1_s=legacy_cruise_sfc,
        reference_speed_m_s=reference_speed,
    )


def propulsion_energy_metadata(model: PropulsionModel) -> dict:
    """Return the canonical energy-consumption contract for reports and handoffs."""

    if model.type == "jet":
        field = "jet_tsfc_kg_per_n_s"
        unit = "kg/(N*s)"
        value = model.jet_tsfc_kg_per_n_s
        formula = "R = V*(L/D)/(g0*c_T) * ln(W0/W1)"
    else:
        field = "prop_bsfc_kg_per_j"
        unit = "kg/J"
        value = model.prop_bsfc_kg_per_j
        formula = "R = eta_p*(L/D)/(g0*c_P) * ln(W0/W1)"
    return {
        "propulsion_type": model.type,
        "canonical_field": field,
        "value": value,
        "unit": unit,
        "source": model.energy_source,
        "legacy_sfc_cruise_1_s": model.legacy_sfc_cruise_1_s,
        "reference_speed_m_s": model.reference_speed_m_s,
        "prop_efficiency": model.prop_efficiency,
        "range_formula": formula,
    }


def propulsion_model_to_input(model: PropulsionModel) -> dict:
    """Serialize a model without reinterpreting its canonical SFC units."""

    value = {
        "type": model.type,
        "thrust_sl_n": model.thrust_sl_n,
        "power_sl_w": model.power_sl_w,
        "jet_tsfc_kg_per_n_s": model.jet_tsfc_kg_per_n_s,
        "prop_bsfc_kg_per_j": model.prop_bsfc_kg_per_j,
        "prop_efficiency": model.prop_efficiency,
        "jet_lapse_exp": model.jet_lapse_exp,
        "prop_power_lapse_exp": model.prop_power_lapse_exp,
        "mct_to_mto_ratio": model.mct_to_mto_ratio,
        "jet_mach_factor": model.jet_mach_factor,
        "jet_model_method": model.jet_model_method,
        "bypass_ratio": model.bypass_ratio,
        "mil_to_ab_sfc_ratio": model.mil_to_ab_sfc_ratio,
        "tsfc_ab_1_s": model.tsfc_ab_1_s,
        "thrust_map": model.thrust_map,
        "sfc_map": model.sfc_map,
        "resolved_energy_source": model.energy_source,
        "legacy_sfc_cruise_1_s": model.legacy_sfc_cruise_1_s,
        "reference_speed_m_s": model.reference_speed_m_s,
    }
    return {key: item for key, item in value.items() if item is not None}


def with_specific_fuel_consumption(model: PropulsionModel, value: float) -> PropulsionModel:
    """Return the same propulsion model with one canonical energy variable changed."""

    parsed = _positive_float(value, "specific fuel consumption")
    if model.type == "jet":
        return replace(
            model,
            jet_tsfc_kg_per_n_s=parsed,
            energy_source="design_variable",
            legacy_sfc_cruise_1_s=None,
        )
    return replace(
        model,
        prop_bsfc_kg_per_j=parsed,
        energy_source="design_variable",
        legacy_sfc_cruise_1_s=None,
    )


def cruise_fuel_fraction(
    model: PropulsionModel,
    *,
    range_m: float,
    cruise_speed_m_s: float,
    lift_to_drag: float,
) -> float:
    """Breguet cruise fuel fraction using the model's canonical units."""

    if range_m < 0.0 or cruise_speed_m_s <= 0.0 or lift_to_drag <= 0.0:
        raise ValueError("range, cruise speed, and lift-to-drag must be valid.")
    if model.type == "jet":
        if model.jet_tsfc_kg_per_n_s is None:
            raise ValueError("Jet model requires jet_tsfc_kg_per_n_s.")
        exponent = (
            range_m
            * CONST.g0_m_s2
            * model.jet_tsfc_kg_per_n_s
            / (cruise_speed_m_s * lift_to_drag)
        )
    else:
        if model.prop_bsfc_kg_per_j is None:
            raise ValueError("Prop model requires prop_bsfc_kg_per_j.")
        eta = model.prop_efficiency or PROP_EFFICIENCY_DEFAULT
        exponent = range_m * CONST.g0_m_s2 * model.prop_bsfc_kg_per_j / (eta * lift_to_drag)
    return 1.0 - math.exp(-min(exponent, 100.0))


def cruise_range_from_fuel_fraction_m(
    model: PropulsionModel,
    *,
    fuel_fraction: float,
    cruise_speed_m_s: float,
    lift_to_drag: float,
) -> float | None:
    """Invert :func:`cruise_fuel_fraction` with the same propulsion model."""

    if not 0.0 <= fuel_fraction < 1.0 or cruise_speed_m_s <= 0.0 or lift_to_drag <= 0.0:
        return None
    logarithm = -math.log(max(1e-12, 1.0 - fuel_fraction))
    if model.type == "jet":
        c_t = model.jet_tsfc_kg_per_n_s
        if c_t is None or c_t <= 0.0:
            return None
        return cruise_speed_m_s * lift_to_drag * logarithm / (CONST.g0_m_s2 * c_t)
    c_p = model.prop_bsfc_kg_per_j
    eta = model.prop_efficiency or PROP_EFFICIENCY_DEFAULT
    if c_p is None or c_p <= 0.0:
        return None
    return eta * lift_to_drag * logarithm / (CONST.g0_m_s2 * c_p)


def _calculate_mattingly_thrust_factor(
    mach: float,
    theta: float,
    delta: float,
    afterburner: bool = False,
) -> float:
    # Mattingly low-bypass turbofan model (2000+ technology)
    # Reference: docs/theory/04_engine_characteristics.md

    # theta = T / T_sl
    # delta = P / P_sl
    # TR = theta (approx for static T_sl)

    # The formulas in the theory document use (M-1) which appears to be a typo
    # for M, because at M=0, T should equal T_sl (alpha=1).
    # If we use (M-1), at M=0, alpha != 1.
    # We assume the formulas are polynomials in M.
    m_val = mach

    if afterburner:
        # α_afterburner = (1 - 0.3M + 0.2M^2) * (δ / θ^0.8)^0.7
        term1 = 1.0 - 0.3 * m_val + 0.2 * (m_val**2)
        term2 = (delta / (theta**0.8)) ** 0.7
        alpha = term1 * term2
    else:
        # α_mil = (1 - 0.6M + 0.1M^2) * (δ / θ^0.8)^0.7
        term1 = 1.0 - 0.6 * m_val + 0.1 * (m_val**2)
        term2 = (delta / (theta**0.8)) ** 0.7
        alpha = term1 * term2

    return max(0.0, alpha)


def _calculate_turbo_ramjet_thrust_factor(mach: float, theta: float, delta: float, afterburner: bool = True) -> float:
    """
    Simulated High-Speed Turbojet / Turbo-Ramjet (J58 class).
    Thrust increases with Mach up to M=3.2 due to ram recovery.
    """
    # Base lapse (Standard Jet)
    # Standard jet drops as sigma^0.7 approx.
    # But Ram recovery P2/P1 ~ (1 + 0.2 M^2)^3.5
    # For a J58, Thrust at M=3.0 is approx equal to Thrust SL Static (or higher).

    # Empirical fit for "High Mach Turbojet":
    # 0 < M < 1: Standard drop
    # 1 < M < 3: Recovery gain
    # M > 3.5: Drop due to thermal limits

    # Let's model it as:
    # Alpha = (delta / theta) * (1 + 0.5 * M^2)  <-- Rough Ram effect
    # But limited by engine structural limits.

    # Simplified Curve for Design Skill:
    # 1. Start with SL Thrust (1.0)
    # 2. At Altitude, density drops.
    # 3. But Velocity increases momentum flux.
    # 4. Ram pressure increases mass flow density.

    # Let's use a piecewise linear factor on top of the standard lapse?
    # No, standard lapse is too punishing for M=3.

    # Use a direct correlation for "High Speed Jet" alpha (T/Tsl):
    # Based on SR-71 performance charts (approx):
    # 30k ft, M=0.9: Thrust ~ 0.4 Tsl
    # 80k ft, M=3.2: Thrust ~ 0.2 Tsl ??
    # Wait, Drag at M=3.2 is high.
    # Actually, J58 T_sl = 34k. Cruise Thrust ~ 7k per engine? (L/D=6, W=100k -> D=16k. 8k/eng).
    # So T_cruise / T_sl = 8/34 = 0.23.
    # But this is at 80k ft! Sigma at 80k is ~0.03.
    # So Thrust/Sigma ~ 0.23 / 0.03 = 7.6 !!
    # Normal jet T/Sigma ~ 1.0.
    # So Mach effect provides a 7x multiplier at M=3.2.

    # Formula:
    # T_avail = T_sl * sigma * (1 + C * M^2)
    # If C = 0.6, at M=3.2 -> 1 + 0.6*10 = 7.
    # This matches nicely!

    # Altitude lapse
    # Sigma (density ratio)
    # For Turbo-Ramjet, it's roughly proportional to ambient pressure (delta) or density (sigma).
    # Let's use Delta (pressure ratio) for Ramjets usually.
    # But let's stick to sigma for consistency with other models unless specialized.
    # Mattingly uses (delta / theta^0.8)^0.7

    # Let's use:
    # Alpha = (delta / theta) * mach_factor
    # This mimics constant corrected thrust?

    # Let's just use the sigma * mach_factor model which is robust and tunable.
    return 0.0  # Not used directly, integrated in main func


def _interpolate_map(map_data: dict, mach: float, altitude_m: float) -> float:
    """
    Bilinear interpolation for map data.
    Expected map format:
    {
        "mach_points": [m0, m1, ...],  # Sorted ascending
        "altitude_points_m": [h0, h1, ...], # Sorted ascending
        "values": [[v_m0_h0, v_m0_h1...], [v_m1_h0...]] # Shape (n_mach, n_alt)
    }
    """
    m_points = map_data.get("mach_points", [])
    h_points = map_data.get("altitude_points_m", [])
    values = map_data.get("values", [])

    if not m_points or not h_points or not values:
        return 0.0

    # Clamp inputs
    m = max(m_points[0], min(m_points[-1], mach))
    h = max(h_points[0], min(h_points[-1], altitude_m))

    # Find indices
    i = bisect.bisect_right(m_points, m) - 1
    j = bisect.bisect_right(h_points, h) - 1

    # Handle edges/clamping logic of bisect
    if i < 0:
        i = 0
    if j < 0:
        j = 0
    if i >= len(m_points) - 1:
        i = len(m_points) - 2
    if j >= len(h_points) - 1:
        j = len(h_points) - 2

    # Interpolate
    m0, m1 = m_points[i], m_points[i + 1]
    h0, h1 = h_points[j], h_points[j + 1]

    # Normalize coords (0..1)
    tm = (m - m0) / (m1 - m0) if m1 > m0 else 0.0
    th = (h - h0) / (h1 - h0) if h1 > h0 else 0.0

    # Bilinear
    # values[i] is row for m_points[i]
    # values[i][j] is value at m_points[i], h_points[j]

    try:
        v00 = values[i][j]
        v01 = values[i][j + 1]
        v10 = values[i + 1][j]
        v11 = values[i + 1][j + 1]
    except IndexError:
        # Fallback if map is malformed
        return values[0][0] if values and values[0] else 0.0

    # Interpolate in Mach first (along columns)
    v0 = v00 * (1 - tm) + v10 * tm
    v1 = v01 * (1 - tm) + v11 * tm

    # Interpolate in Alt
    val = v0 * (1 - th) + v1 * th

    return val


def thrust_available_n(
    model: PropulsionModel, *, altitude_m: float, speed_m_s: float, isa_delta_c: float = 0.0, rating: str = "mto"
) -> float:
    atm = isa_tropopause(altitude_m, delta_t_k=float(isa_delta_c))
    sigma = atm.rho_kg_m3 / CONST.rho0_kg_m3

    # Rating factor
    r_factor = 1.0
    if rating in ["mct", "max_continuous", "cruise", "climb"]:
        r_factor = model.mct_to_mto_ratio

    if model.type == "jet":
        mach = speed_m_s / atm.a_m_s

        if model.thrust_map:
            t_avail = _interpolate_map(model.thrust_map, mach, altitude_m)
            return t_avail * r_factor

        if model.thrust_sl_n is None:
            raise ValueError("Jet model requires thrust_sl_n.")

        if model.jet_model_method == "mattingly_low_bypass":
            # ... (existing mattingly code)
            theta = atm.t_k / 288.15
            delta = atm.p_pa / 101325.0
            use_ab = rating == "mto"
            alpha = _calculate_mattingly_thrust_factor(mach, theta, delta, afterburner=use_ab)
            if not use_ab:
                # Recalculate alpha for Mil (approx)
                alpha = _calculate_mattingly_thrust_factor(mach, theta, delta, afterburner=False)
                alpha *= r_factor
            return model.thrust_sl_n * alpha

        elif model.jet_model_method == "turbo_ramjet":
            # High speed model (T ~ Sigma * (1 + 0.7 M^2))
            # Matches SR-71 behavior roughly.
            # T_avail = T_sl * (P/P0) * (1 + 0.6 M^2)
            # Using Sigma approx P/P0 at isothermal stratosphere

            mach_factor = 1.0 + 0.6 * (mach**2.0)

            # For Ramjets, Thrust is zero at M=0?
            # No, this is a Turbo-Ramjet (J58), so it has static thrust.

            # Cutoff or limit?
            # J58 inlet recovery drops after M=3.2.
            # Let's add a rolloff > M=3.5
            if mach > 3.5:
                mach_factor *= max(0.0, 1.0 - (mach - 3.5))

            thrust = model.thrust_sl_n * sigma * mach_factor * r_factor
            return thrust

        else:
            # Simple model
            mach_corr = 1.0 + model.jet_mach_factor * mach
            return model.thrust_sl_n * (sigma**model.jet_lapse_exp) * mach_corr * r_factor

    if model.type == "prop":
        if model.power_sl_w is None:
            if model.thrust_sl_n is None:
                raise ValueError("Prop model requires power_sl_w or thrust_sl_n.")
            # If thrust_sl_n is given, assume it behaves like constant thrust (unlikely for prop) or simplified
            return model.thrust_sl_n * r_factor

        p_avail = model.power_sl_w * (sigma**model.prop_power_lapse_exp) * r_factor
        eta = model.prop_efficiency if model.prop_efficiency is not None else 0.8
        v = max(1.0, speed_m_s)
        return eta * p_avail / v

    raise ValueError("propulsion.type must be 'jet' or 'prop'.")


def _calculate_mattingly_sfc_factor(
    mach: float,
    theta: float,
    afterburner: bool = False,
) -> float:
    # Mattingly low-bypass turbofan SFC model
    # Reference: docs/theory/04_engine_characteristics.md

    # We use M instead of (M-1) to ensure factor=1.0 at M=0 (Static)
    m_val = mach

    if afterburner:
        # SFC_ab = SFC_SL * (1 + 0.5M) * θ^0.5
        factor = (1.0 + 0.5 * m_val) * (theta**0.5)
    else:
        # SFC_mil = SFC_SL * (1 - 0.3M + 0.1M^2) * θ^0.5
        factor = (1.0 - 0.3 * m_val + 0.1 * (m_val**2)) * (theta**0.5)

    return factor


def fuel_flow_n_s(
    model: PropulsionModel,
    *,
    thrust_n: float,
    shaft_power_w: float | None = None,
    altitude_m: float = 0.0,
    speed_m_s: float = 0.0,
    isa_delta_c: float = 0.0,
) -> float:
    if model.type == "jet":
        if model.jet_tsfc_kg_per_n_s is None:
            raise ValueError("Jet model requires jet_tsfc_kg_per_n_s.")

        sfc = model.jet_tsfc_kg_per_n_s

        if model.jet_model_method == "mattingly_low_bypass":
            # Mattingly Model with AB logic
            atm = isa_tropopause(altitude_m, delta_t_k=float(isa_delta_c))
            mach = speed_m_s / atm.a_m_s
            theta = atm.t_k / 288.15

            # Calculate Mil Thrust Available to determine if AB is needed
            # We assume mct_to_mto_ratio represents Mil/AB ratio if AB is present
            try:
                t_mil_avail = thrust_available_n(
                    model, altitude_m=altitude_m, speed_m_s=speed_m_s, isa_delta_c=isa_delta_c, rating="mct"
                )
            except Exception:
                t_mil_avail = 1.0  # Safe fallback

            # Check if we need AB
            if thrust_n > t_mil_avail and t_mil_avail > 1.0:
                # AB Regime
                # Use AB SFC factor
                factor = _calculate_mattingly_sfc_factor(mach, theta, afterburner=True)
                sfc = model.jet_tsfc_kg_per_n_s * factor * model.mil_to_ab_sfc_ratio
                # We don't apply throttle correction for AB in this simple model
            else:
                # Mil Regime
                throttle = min(1.0, max(0.0, thrust_n / t_mil_avail)) if t_mil_avail > 1.0 else 1.0
                factor = _calculate_mattingly_sfc_factor(mach, theta, afterburner=False)
                sfc = model.jet_tsfc_kg_per_n_s * factor

                # Throttle correction for Mil (partial power)
                sfc_throttle_factor = 1.0 + 0.2 * (1.0 - throttle)
                sfc *= sfc_throttle_factor

        return sfc * max(0.0, thrust_n) * CONST.g0_m_s2

    if model.type == "prop":
        if model.prop_bsfc_kg_per_j is None:
            raise ValueError("Prop model requires prop_bsfc_kg_per_j.")
        if shaft_power_w is None:
            raise ValueError("Prop model requires shaft_power_w for fuel flow.")
        return model.prop_bsfc_kg_per_j * max(0.0, shaft_power_w) * CONST.g0_m_s2
    raise ValueError("propulsion.type must be 'jet' or 'prop'.")


def calculate_turbofan_thrust(
    *,
    thrust_sl_n: float,
    mach: float,
    altitude_m: float,
    throttle_position: float = 1.0,
    bypass_ratio: float = 6.0,
    isa_delta_c: float = 0.0,
) -> dict:
    from ..common.atmosphere import isa_tropopause
    from ..common.units import CONST

    if thrust_sl_n <= 0.0:
        raise ValueError("thrust_sl_n must be positive.")
    if throttle_position < 0.0 or throttle_position > 1.0:
        raise ValueError("throttle_position must be in [0, 1].")

    atm = isa_tropopause(altitude_m, delta_t_k=float(isa_delta_c))
    sigma = atm.rho_kg_m3 / CONST.rho0_kg_m3

    alpha = 0.7 + 0.1 * (1.0 - bypass_ratio / 10.0)

    thrust_available_n = thrust_sl_n * (sigma**alpha) * throttle_position

    mach_factor = 1.0 + 0.3 * mach
    thrust_available_n *= mach_factor

    return {
        "thrust_available_n": thrust_available_n,
        "thrust_sl_n": thrust_sl_n,
        "mach": mach,
        "altitude_m": altitude_m,
        "throttle_position": throttle_position,
        "sigma": sigma,
        "alpha": alpha,
        "bypass_ratio": bypass_ratio,
    }


def calculate_turbofan_sfc(
    *,
    sfc_sl: float,
    mach: float,
    altitude_m: float,
    throttle_position: float = 1.0,
    bypass_ratio: float = 6.0,
    isa_delta_c: float = 0.0,
) -> dict:
    from ..common.atmosphere import isa_tropopause
    from ..common.units import CONST

    if sfc_sl <= 0.0:
        raise ValueError("sfc_sl must be positive.")
    if throttle_position < 0.0 or throttle_position > 1.0:
        raise ValueError("throttle_position must be in [0, 1].")

    atm = isa_tropopause(altitude_m, delta_t_k=float(isa_delta_c))
    sigma = atm.rho_kg_m3 / CONST.rho0_kg_m3

    beta = 0.8 + 0.1 * (1.0 - bypass_ratio / 10.0)

    sfc_available = sfc_sl * (sigma**beta) * (1.0 + 0.5 * (1.0 - throttle_position))

    mach_factor = 1.0 + 0.2 * mach
    sfc_available *= mach_factor

    return {
        "sfc_available": sfc_available,
        "sfc_sl": sfc_sl,
        "mach": mach,
        "altitude_m": altitude_m,
        "throttle_position": throttle_position,
        "sigma": sigma,
        "beta": beta,
        "bypass_ratio": bypass_ratio,
    }


def generate_thrust_envelope(
    *,
    thrust_sl_n: float,
    mach_range: list[float],
    altitude_range: list[float],
    throttle_position: float = 1.0,
    bypass_ratio: float = 6.0,
    isa_delta_c: float = 0.0,
) -> dict:
    thrust_grid: list[list[float]] = []

    for mach in mach_range:
        thrust_row: list[float] = []
        for altitude in altitude_range:
            result = calculate_turbofan_thrust(
                thrust_sl_n=thrust_sl_n,
                mach=mach,
                altitude_m=altitude,
                throttle_position=throttle_position,
                bypass_ratio=bypass_ratio,
                isa_delta_c=isa_delta_c,
            )
            thrust_row.append(result["thrust_available_n"])
        thrust_grid.append(thrust_row)

    return {
        "mach": mach_range,
        "altitude_m": altitude_range,
        "thrust_n": thrust_grid,
    }


def generate_sfc_envelope(
    *,
    sfc_sl: float,
    mach_range: list[float],
    altitude_range: list[float],
    throttle_position: float = 1.0,
    bypass_ratio: float = 6.0,
    isa_delta_c: float = 0.0,
) -> dict:
    sfc_grid: list[list[float]] = []

    for mach in mach_range:
        sfc_row: list[float] = []
        for altitude in altitude_range:
            result = calculate_turbofan_sfc(
                sfc_sl=sfc_sl,
                mach=mach,
                altitude_m=altitude,
                throttle_position=throttle_position,
                bypass_ratio=bypass_ratio,
                isa_delta_c=isa_delta_c,
            )
            sfc_row.append(result["sfc_available"])
        sfc_grid.append(sfc_row)

    return {
        "mach": mach_range,
        "altitude_m": altitude_range,
        "sfc": sfc_grid,
    }
