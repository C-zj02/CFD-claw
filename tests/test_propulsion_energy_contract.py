"""Unit and cross-stage regressions for the propulsion energy contract."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

from src.design_execution import AircraftDesignRequest, AircraftDesignRunner


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_ROOT = PROJECT_ROOT / "external" / "aircraft-design-skill"
if str(UPSTREAM_ROOT) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_ROOT))

from aircraft_design.class2_preliminary.propulsion import (  # noqa: E402
    build_propulsion_model,
    cruise_fuel_fraction,
    cruise_range_from_fuel_fraction_m,
    fuel_flow_n_s,
    propulsion_energy_metadata,
)
from aircraft_design.common.units import CONST  # noqa: E402


def _request(propulsion_type: str, **initial_guess) -> AircraftDesignRequest:
    return AircraftDesignRequest.from_dict(
        {
            "project_name": f"energy_{propulsion_type}",
            "requirements": {
                "range_m": 300_000.0,
                "payload_kg": 100.0,
                "cruise_mach": 0.22 if propulsion_type == "prop" else 0.72,
                "cruise_altitude_m": 3_000.0 if propulsion_type == "prop" else 10_000.0,
                "service_ceiling_m": 6_000.0 if propulsion_type == "prop" else 14_000.0,
                "propulsion_type": propulsion_type,
            },
            **({"initial_guess": initial_guess} if initial_guess else {}),
        }
    )


def test_prop_and_jet_defaults_use_distinct_canonical_units() -> None:
    prop = _request("prop")
    jet = _request("jet")

    assert prop.initial_guess.sfc_cruise_1_s is None
    assert prop.initial_guess.prop_bsfc_kg_per_j == pytest.approx(8.45e-8)
    assert prop.initial_guess.jet_tsfc_kg_per_n_s is None
    assert prop.provenance["propulsion_energy"] == {
        "propulsion_type": "prop",
        "canonical_field": "prop_bsfc_kg_per_j",
        "source": "default",
        "legacy_field": None,
        "legacy_semantics": None,
    }

    assert jet.initial_guess.sfc_cruise_1_s is None
    assert jet.initial_guess.jet_tsfc_kg_per_n_s == pytest.approx(2.3e-5)
    assert jet.initial_guess.prop_bsfc_kg_per_j is None
    assert jet.provenance["propulsion_energy"]["canonical_field"] == "jet_tsfc_kg_per_n_s"
    assert jet.provenance["propulsion_energy"]["source"] == "default"


def test_fuel_flow_uses_mass_tsfc_for_jet_and_bsfc_for_prop() -> None:
    jet_tsfc = 2.5e-5
    prop_bsfc = 8.0e-8
    thrust_n = 12_000.0
    shaft_power_w = 250_000.0
    jet = build_propulsion_model(
        {"type": "jet", "thrust_sl_n": 20_000.0, "jet_tsfc_kg_per_n_s": jet_tsfc}
    )
    prop = build_propulsion_model(
        {
            "type": "prop",
            "power_sl_w": 300_000.0,
            "prop_bsfc_kg_per_j": prop_bsfc,
            "prop_efficiency": 0.82,
        }
    )

    assert fuel_flow_n_s(jet, thrust_n=thrust_n) == pytest.approx(
        jet_tsfc * thrust_n * CONST.g0_m_s2
    )
    assert fuel_flow_n_s(prop, thrust_n=0.0, shaft_power_w=shaft_power_w) == pytest.approx(
        prop_bsfc * shaft_power_w * CONST.g0_m_s2
    )
    assert propulsion_energy_metadata(jet)["unit"] == "kg/(N*s)"
    assert propulsion_energy_metadata(prop)["unit"] == "kg/J"


def test_propeller_efficiency_above_unity_is_rejected() -> None:
    with pytest.raises(ValueError, match="prop_efficiency must be <= 1.0"):
        build_propulsion_model(
            {
                "type": "prop",
                "prop_bsfc_kg_per_j": 8.45e-8,
                "prop_efficiency": 1.01,
            }
        )


@pytest.mark.parametrize("propulsion_type", ["jet", "prop"])
def test_breguet_fuel_fraction_and_range_are_inverse_in_canonical_units(
    propulsion_type: str,
) -> None:
    speed = 95.0
    lift_to_drag = 13.0
    range_m = 650_000.0
    if propulsion_type == "jet":
        model = build_propulsion_model(
            {"type": "jet", "jet_tsfc_kg_per_n_s": 2.4e-5}
        )
        expected_exponent = (
            range_m * CONST.g0_m_s2 * 2.4e-5 / (speed * lift_to_drag)
        )
    else:
        model = build_propulsion_model(
            {
                "type": "prop",
                "prop_bsfc_kg_per_j": 8.45e-8,
                "prop_efficiency": 0.8,
            }
        )
        expected_exponent = range_m * CONST.g0_m_s2 * 8.45e-8 / (0.8 * lift_to_drag)

    fraction = cruise_fuel_fraction(
        model,
        range_m=range_m,
        cruise_speed_m_s=speed,
        lift_to_drag=lift_to_drag,
    )

    assert fraction == pytest.approx(1.0 - math.exp(-expected_exponent))
    assert cruise_range_from_fuel_fraction_m(
        model,
        fuel_fraction=fraction,
        cruise_speed_m_s=speed,
        lift_to_drag=lift_to_drag,
    ) == pytest.approx(range_m)


@pytest.mark.parametrize("propulsion_type", ["jet", "prop"])
def test_legacy_sfc_migration_preserves_historical_cruise_exponent(
    propulsion_type: str,
) -> None:
    legacy = 0.8 / 3_600.0
    speed = 80.0
    eta = 0.78
    lift_to_drag = 12.0
    range_m = 400_000.0
    model = build_propulsion_model(
        {
            "type": propulsion_type,
            "legacy_sfc_cruise_1_s": legacy,
            "reference_speed_m_s": speed,
            "prop_efficiency": eta,
        }
    )

    if propulsion_type == "jet":
        assert model.jet_tsfc_kg_per_n_s == pytest.approx(legacy / CONST.g0_m_s2)
    else:
        assert model.prop_bsfc_kg_per_j == pytest.approx(
            legacy * eta / (CONST.g0_m_s2 * speed)
        )
    expected = 1.0 - math.exp(-range_m * legacy / (speed * lift_to_drag))
    assert cruise_fuel_fraction(
        model,
        range_m=range_m,
        cruise_speed_m_s=speed,
        lift_to_drag=lift_to_drag,
    ) == pytest.approx(expected)
    assert propulsion_energy_metadata(model)["source"] == "legacy_sfc_cruise_1_s_migrated"


def test_real_workflow_reuses_prop_energy_contract_across_class1_advanced_and_oat(
    tmp_path: Path,
) -> None:
    request = AircraftDesignRequest.from_dict(
        {
            "project_name": "shared_propulsion_contract",
            "requirements": {
                "range_m": 100_000.0,
                "payload_kg": 5.0,
                "cruise_mach": 0.07,
                "cruise_altitude_m": 1_000.0,
                "takeoff_distance_m": 150.0,
                "landing_distance_m": 150.0,
                "service_ceiling_m": 3_000.0,
                "propulsion_type": "prop",
                "assumed_climb_rate_m_s": 3.0,
            },
            "initial_guess": {
                "prop_bsfc_kg_per_j": 8.2e-8,
                "prop_efficiency": 0.81,
            },
        }
    )
    runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=tmp_path / "runs")

    result = runner.run(request, timeout_seconds=30.0, run_id="shared-energy")

    energy = result.design_data["outputs"]["propulsion_energy"]
    advanced = result.design_data["advanced_results"]
    assert energy["canonical_field"] == "prop_bsfc_kg_per_j"
    assert energy["value"] == pytest.approx(8.2e-8)
    assert energy["unit"] == "kg/J"
    assert energy["source"] == "user"
    assert result.design_data["provenance"]["propulsion_energy"] == energy
    assert advanced["stage3_propulsion"]["propulsion_energy"] == energy
    assert advanced["stage4_mission"]["propulsion_energy"] == energy

    optimization = advanced["stage7_optimization"]
    assert "prop_bsfc_kg_per_j" in optimization["sensitivity_analysis"]
    assert optimization["sensitivity_analysis"]["prop_bsfc_kg_per_j"]["method"] == "one_at_a_time"
    for case in optimization["sensitivity_analysis"]["prop_bsfc_kg_per_j"]["cases"]:
        assert case["metrics"]["propulsion_energy"]["canonical_field"] == "prop_bsfc_kg_per_j"
        assert case["metrics"]["evaluation_scope"] == "reduced_order_screening"
        assert case["metrics"]["engineering_revalidation_performed"] is False
