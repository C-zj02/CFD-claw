import argparse
import copy
import sys
import io
import shutil
import socket
import json
import math
import re
import struct
from dataclasses import asdict
from pathlib import Path
from datetime import datetime

from .design_loop_orchestrator import (
    DesignRequirements,
    InitialGuess,
    sizing_loop,
)
from .visualization_realtime import RealTimeVisualizer
from ..utils.report_generator_v2 import ReportGeneratorV2
from ..utils.report_generator_extended import ReportGeneratorExtended
from ..utils.report_generator_unified import UnifiedReportGenerator
from ..utils.visualization_static import StaticPlotter
from ..utils.chart_data_generator import ChartDataGenerator
from ..utils.visualization_interactive import InteractivePlotter, plot_payload_range, plot_weight_breakdown
from ..utils.visualization_3d import build_mesh_parts_from_geometry, generate_three_view_html, mesh_to_obj
from ..class3_detailed.geometry_detailed import geometry_detailed_from_inputs
from ..class3_detailed.openvsp_bridge import write_openvsp_script
from .visualization_advanced import AdvancedVisualizer
from .advanced_design import AdvancedDesignStageError, execute_advanced_design
from .generate_advanced_report import generate_advanced_design_report
from ..common.atmosphere import isa_tropopause
from ..common.units import CONST
from .geometry_constraints import GeometryConstraintChecker
from .constraints import AeroPolar, normalized_constraint
from .takeoff_landing import landing_distance_over_obstacle_m, takeoff_distance_over_obstacle_m
from .propulsion import (
    build_propulsion_model,
    cruise_fuel_fraction,
    cruise_range_from_fuel_fraction_m,
    propulsion_energy_metadata,
    propulsion_model_to_input,
    with_specific_fuel_consumption,
)
from .result_contract import (
    SCHEMA_ID,
    SCHEMA_VERSION,
    blocking_constraints_passed,
    engineering_feasible,
    normalized_advanced_constraints,
    stage_record,
)
from ..class3_detailed.geometry_modeling import parametric_to_aircraft_geometry
from .system_architecture import estimate_system_weights
from ..class3_detailed.vspaero_interface import run_vspaero_analysis


class TeeStream(io.TextIOBase):
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def write(self, s):
        self.primary.write(s)
        self.primary.flush()
        if not self.secondary.closed:
            try:
                self.secondary.write(s)
                self.secondary.flush()
            except ValueError:
                pass
        return len(s)

    def flush(self):
        self.primary.flush()
        if not self.secondary.closed:
            try:
                self.secondary.flush()
            except ValueError:
                pass

    def isatty(self):
        return self.primary.isatty()


def send_report_path_to_gui(path: Path):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1.0)
        client.connect(("localhost", 9999))

        msg = {"type": "report_generated", "path": str(path), "__protocol__": "json", "__version__": 1}
        data = json.dumps(msg, ensure_ascii=False).encode("utf-8")
        length = struct.pack(">I", len(data))

        client.sendall(length + data)
        client.close()
        print(f"Sent report path to GUI: {path}")
    except Exception:
        pass


def setup_output_directory(base_dir: str = "output", project_name: str = "design") -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_project_name = re.sub(r"[^A-Za-z0-9_-]+", "_", str(project_name)).strip("_-") or "design"
    output_base = Path(base_dir).expanduser().resolve()
    output_path = (output_base / f"{safe_project_name}_{timestamp}").resolve()
    try:
        output_path.relative_to(output_base)
    except ValueError as exc:
        raise ValueError("output directory must remain inside output_base") from exc
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def _configuration_value(data: dict, requirements: dict, key: str, default):
    if key in requirements:
        return requirements[key]
    configuration = data.get("configuration", {})
    if isinstance(configuration, dict) and key in configuration:
        return configuration[key]
    return data.get(key, default)


def _provided_configuration(data: dict, requirements: dict) -> dict:
    provided = dict(requirements)
    configuration = data.get("configuration", {})
    if isinstance(configuration, dict):
        provided.update(configuration)
    for key in (
        "aircraft_role",
        "propulsion_type",
        "reserve_fraction",
        "tail_layout",
        "cl_max_takeoff",
        "cl_max_landing",
        "assumed_climb_rate_m_s",
        "uncertainty_enabled",
    ):
        if key in data:
            provided[key] = data[key]
    provided.update(requirements)
    return provided


def _input_provenance(
    values: dict,
    provided: dict,
    defaults: dict,
    declared: dict | None = None,
) -> dict:
    result: dict = {}
    declared = declared if isinstance(declared, dict) else {}
    for key, value in values.items():
        raw_record = declared.get(key)
        record = copy.deepcopy(raw_record) if isinstance(raw_record, dict) else {}
        source = record.get("source")
        if not isinstance(source, str) or not source.strip():
            source = "user" if key in provided else "default"
        record["source"] = source
        record["value"] = value
        if key in defaults:
            record.setdefault("default", defaults[key])
        result[key] = record
    return result


def _refresh_contract_status(output_data: dict) -> None:
    numerical_converged = bool(output_data.get("numerical_converged"))
    constraints = output_data.get("constraints", [])
    stage_status = output_data.get("stage_status", {})
    feasible = engineering_feasible(
        numerical_converged=numerical_converged,
        constraints=constraints,
        stage_status=stage_status,
    )
    output_data["engineering_feasible"] = feasible
    output_data["outputs"]["engineering_feasible"] = feasible
    output_data["outputs"]["numerical_converged"] = numerical_converged
    output_data["outputs"]["converged"] = numerical_converged
    failed_constraints = [c for c in constraints if c.get("blocking") and not c.get("passed")]
    if not numerical_converged:
        task_status = "not_converged"
        summary = "The last valid Class I estimate was preserved, but numerical convergence was not achieved."
    elif feasible:
        task_status = "completed"
        summary = "Numerical convergence and all blocking engineering gates passed."
    else:
        task_status = "completed_with_issues"
        summary = f"Numerical convergence completed with {len(failed_constraints)} failed blocking engineering constraint(s)."
    output_data["status"] = {
        "task_status": task_status,
        "numerical_converged": numerical_converged,
        "engineering_feasible": feasible,
        "blocking_constraints_passed": blocking_constraints_passed(constraints),
        "summary": summary,
    }


def _shared_propulsion_model(data: dict, req: DesignRequirements, guess: InitialGuess):
    """Resolve one canonical energy model for every stage of this run."""

    configured = data.get("propulsion", {})
    propulsion_input = dict(configured) if isinstance(configured, dict) else {}
    cruise_atmosphere = isa_tropopause(req.cruise_altitude_m, delta_t_k=float(req.isa_delta_c))
    cruise_speed_m_s = req.cruise_mach * cruise_atmosphere.a_m_s
    propulsion_input["type"] = req.propulsion_type
    propulsion_input.setdefault("thrust_sl_n", guess.mtow_kg * CONST.g0_m_s2 * guess.thrust_to_weight)
    propulsion_input.setdefault("jet_tsfc_kg_per_n_s", guess.jet_tsfc_kg_per_n_s)
    propulsion_input.setdefault("prop_bsfc_kg_per_j", guess.prop_bsfc_kg_per_j)
    propulsion_input.setdefault("prop_efficiency", guess.prop_efficiency)
    propulsion_input.setdefault("legacy_sfc_cruise_1_s", guess.sfc_cruise_1_s)
    propulsion_input.setdefault("reference_speed_m_s", cruise_speed_m_s)
    configured_energy_fields = {
        "jet_tsfc_kg_per_n_s",
        "tsfc_kg_per_n_s",
        "tsfc_1_s",
        "prop_bsfc_kg_per_j",
        "bsfc_kg_per_j",
        "sfc_1_s",
    }
    declared_energy = data.get("provenance", {})
    if isinstance(declared_energy, dict):
        declared_energy = declared_energy.get("propulsion_energy", {})
    if (
        isinstance(declared_energy, dict)
        and not configured_energy_fields.intersection(configured)
        and declared_energy.get("source") in {"user", "default"}
    ):
        propulsion_input.setdefault("resolved_energy_source", declared_energy["source"])
    return build_propulsion_model(propulsion_input)


def main():
    parser = argparse.ArgumentParser(description="Run Fixed Wing Class I Sizing Loop")
    parser.add_argument("input_file", type=Path, help="Path to input JSON file")
    parser.add_argument("--project-name", "-n", type=str, default="aircraft_sizing", help="Name of the project")
    parser.add_argument("--output-dir", "-o", type=Path, default=Path("output"), help="Base directory for outputs")
    parser.add_argument("--no-viz", action="store_true", help="Disable real-time visualization")
    parser.add_argument("--viz-port", type=int, default=9999, help="Port for visualization server")

    args = parser.parse_args()
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    log_file = None

    if not args.input_file.exists():
        print(f"Error: Input file {args.input_file} not found.")
        sys.exit(1)

    print("=" * 60)
    print("  Fixed Wing Sizing - Interactive Mode Available")
    print("=" * 60)

    viz = None
    if not args.no_viz:
        print("  Initializing Visualization Environment...")
        viz = RealTimeVisualizer(port=args.viz_port)
        if not viz.start(require_server=True):
            print("  > Visualization server is not running.")
            print(
                f"  > Start it first in another terminal: python -m aircraft_design.gui.server --port {args.viz_port}"
            )
            sys.exit(1)
        print("  > 3D Visualization Server is running.")
        print("  > Real-time updates will be shown in popup window.")
    else:
        print("  > Visualization disabled by user.")

    print("=" * 60)

    try:
        run_dir = setup_output_directory(args.output_dir, args.project_name)
        print(f"Output directory created: {run_dir}")
        log_path = run_dir / "run.log"
        log_file = open(log_path, "a", encoding="utf-8")
        sys.stdout = TeeStream(original_stdout, log_file)
        sys.stderr = TeeStream(original_stderr, log_file)
        print(f"Log file: {log_path}")

        with open(args.input_file, "r") as f:
            data = json.load(f)

        req_data = data.get("requirements", {})
        guess_data = data.get("initial_guess", {})

        req_defaults = {
            "range_m": 2000e3,
            "payload_kg": 1000.0,
            "cruise_mach": 0.8,
            "cruise_altitude_m": 11000.0,
            "takeoff_distance_m": 1000.0,
            "landing_distance_m": 1000.0,
            "stall_speed_m_s": None,
            "max_load_factor": 7.33,
            "sustained_turn_g": 2.0,
            "service_ceiling_m": 15000.0,
            "isa_delta_c": 0.0,
            "assumed_climb_rate_m_s": 50.0,
            "aircraft_role": "light_fighter",
            "propulsion_type": "jet",
            "reserve_fraction": 0.06,
            "tail_layout": "conventional",
            "cl_max_takeoff": 1.4,
            "cl_max_landing": 1.6,
            "obstacle_height_m": None,
            "takeoff_climb_gradient": None,
            "landing_approach_angle_deg": 3.0,
            "landing_decel_g": 0.4,
            "runway_slope": 0.0,
            "headwind_m_s": 0.0,
            "uncertainty_enabled": False,
        }
        guess_defaults = {
            "mtow_kg": 10000.0,
            "thrust_to_weight": 0.6,
            "wing_loading_pa": 3000.0,
            "aspect_ratio": 3.5,
            "sweep_deg": 45.0,
            "taper_ratio": 0.3,
            "thickness_ratio": 0.08,
            "sfc_cruise_1_s": None,
            "jet_tsfc_kg_per_n_s": None,
            "prop_bsfc_kg_per_j": None,
            "prop_efficiency": 0.8,
            "cd0": 0.02,
            "oswald_e": 0.8,
            "cg_fraction_cbar": 0.30,
            "horizontal_tail_volume_coefficient": 0.40,
        }
        provided_req = _provided_configuration(data, req_data)

        req = DesignRequirements(
            range_m=req_data.get("range_m", req_defaults["range_m"]),
            payload_kg=req_data.get("payload_kg", req_defaults["payload_kg"]),
            cruise_mach=req_data.get("cruise_mach", req_defaults["cruise_mach"]),
            cruise_altitude_m=req_data.get("cruise_altitude_m", req_defaults["cruise_altitude_m"]),
            takeoff_distance_m=req_data.get("takeoff_distance_m", req_defaults["takeoff_distance_m"]),
            landing_distance_m=req_data.get("landing_distance_m", req_defaults["landing_distance_m"]),
            stall_speed_m_s=req_data.get("stall_speed_m_s", req_defaults["stall_speed_m_s"]),
            max_load_factor=req_data.get("max_load_factor", req_defaults["max_load_factor"]),
            sustained_turn_g=req_data.get("sustained_turn_g", req_defaults["sustained_turn_g"]),
            service_ceiling_m=req_data.get("service_ceiling_m", req_defaults["service_ceiling_m"]),
            isa_delta_c=req_data.get("isa_delta_c", req_defaults["isa_delta_c"]),
            assumed_climb_rate_m_s=_configuration_value(
                data, req_data, "assumed_climb_rate_m_s", req_defaults["assumed_climb_rate_m_s"]
            ),
            aircraft_role=_configuration_value(data, req_data, "aircraft_role", req_defaults["aircraft_role"]),
            propulsion_type=_configuration_value(data, req_data, "propulsion_type", req_defaults["propulsion_type"]),
            reserve_fraction=_configuration_value(data, req_data, "reserve_fraction", req_defaults["reserve_fraction"]),
            tail_layout=_configuration_value(data, req_data, "tail_layout", req_defaults["tail_layout"]),
            cl_max_takeoff=_configuration_value(data, req_data, "cl_max_takeoff", req_defaults["cl_max_takeoff"]),
            cl_max_landing=_configuration_value(data, req_data, "cl_max_landing", req_defaults["cl_max_landing"]),
            obstacle_height_m=req_data.get("obstacle_height_m", req_defaults["obstacle_height_m"]),
            takeoff_climb_gradient=req_data.get("takeoff_climb_gradient", req_defaults["takeoff_climb_gradient"]),
            landing_approach_angle_deg=req_data.get(
                "landing_approach_angle_deg", req_defaults["landing_approach_angle_deg"]
            ),
            landing_decel_g=req_data.get("landing_decel_g", req_defaults["landing_decel_g"]),
            runway_slope=req_data.get("runway_slope", req_defaults["runway_slope"]),
            headwind_m_s=req_data.get("headwind_m_s", req_defaults["headwind_m_s"]),
            uncertainty_enabled=bool(
                _configuration_value(data, req_data, "uncertainty_enabled", req_defaults["uncertainty_enabled"])
            ),
        )

        if req.propulsion_type == "jet":
            guess_defaults["jet_tsfc_kg_per_n_s"] = 2.3e-5
        else:
            guess_defaults["prop_bsfc_kg_per_j"] = 8.45e-8
        legacy_sfc_provided = guess_data.get("sfc_cruise_1_s") is not None
        canonical_energy_field = (
            "jet_tsfc_kg_per_n_s" if req.propulsion_type == "jet" else "prop_bsfc_kg_per_j"
        )
        if legacy_sfc_provided and guess_data.get(canonical_energy_field) is None:
            guess_defaults[canonical_energy_field] = None

        guess = InitialGuess(
            mtow_kg=guess_data.get("mtow_kg", guess_defaults["mtow_kg"]),
            thrust_to_weight=guess_data.get("thrust_to_weight", guess_defaults["thrust_to_weight"]),
            wing_loading_pa=guess_data.get("wing_loading_pa", guess_defaults["wing_loading_pa"]),
            aspect_ratio=guess_data.get("aspect_ratio", guess_defaults["aspect_ratio"]),
            sweep_deg=guess_data.get("sweep_deg", guess_defaults["sweep_deg"]),
            taper_ratio=guess_data.get("taper_ratio", guess_defaults["taper_ratio"]),
            thickness_ratio=guess_data.get("thickness_ratio", guess_defaults["thickness_ratio"]),
            sfc_cruise_1_s=guess_data.get("sfc_cruise_1_s", guess_defaults["sfc_cruise_1_s"]),
            jet_tsfc_kg_per_n_s=guess_data.get(
                "jet_tsfc_kg_per_n_s", guess_defaults["jet_tsfc_kg_per_n_s"]
            ),
            prop_bsfc_kg_per_j=guess_data.get(
                "prop_bsfc_kg_per_j", guess_defaults["prop_bsfc_kg_per_j"]
            ),
            prop_efficiency=guess_data.get("prop_efficiency", guess_defaults["prop_efficiency"]),
            cd0=guess_data.get("cd0", guess_defaults["cd0"]),
            oswald_e=guess_data.get("oswald_e", guess_defaults["oswald_e"]),
            cg_fraction_cbar=guess_data.get(
                "cg_fraction_cbar", guess_defaults["cg_fraction_cbar"]
            ),
            horizontal_tail_volume_coefficient=guess_data.get(
                "horizontal_tail_volume_coefficient",
                guess_defaults["horizontal_tail_volume_coefficient"],
            ),
        )

        if req.propulsion_type not in {"jet", "prop"}:
            raise ValueError("requirements.propulsion_type must be 'jet' or 'prop'.")
        if not 0.0 <= req.reserve_fraction < 1.0:
            raise ValueError("requirements.reserve_fraction must be in [0, 1).")

        print("Starting Sizing Loop...")

        solver_options = data.get("solver_options", {})
        if not isinstance(solver_options, dict):
            raise ValueError("solver_options must be an object.")
        shared_propulsion_model = _shared_propulsion_model(data, req, guess)
        shared_propulsion_energy = propulsion_energy_metadata(shared_propulsion_model)

        result = sizing_loop(
            req,
            guess,
            propulsion_model=shared_propulsion_model,
            enable_visualization=not args.no_viz,
            visualizer=viz,
            tolerance=solver_options.get("tolerance", 1e-3),
            max_iter=solver_options.get("max_iter", 50),
        )

        stage_status = dict(result.stage_status)
        downstream_reason = "Awaiting the converged Class I result." if result.converged else "Skipped because Class I did not converge."
        stage_status.update(
            {
                "geometry": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage2_aero": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage3_propulsion": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage4_mission": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage5_stability": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage6_structures": stage_record("skipped", blocking=True, message=downstream_reason),
                "stage7_optimization": stage_record("skipped", blocking=False, message=downstream_reason),
                "uncertainty": stage_record(
                    "skipped",
                    blocking=False,
                    message=(
                        "Awaiting the nominal design result."
                        if req.uncertainty_enabled and result.converged
                        else "Deterministic uncertainty analysis was not requested."
                    ),
                ),
            }
        )
        generated_at = datetime.now().isoformat()
        user_provenance = data.get("provenance", {})
        if not isinstance(user_provenance, dict):
            user_provenance = {"provided_value": user_provenance}
        declared_input_fields = user_provenance.get("input_fields", {})
        if not isinstance(declared_input_fields, dict):
            declared_input_fields = {}
        declared_requirements = declared_input_fields.get("requirements", {})
        declared_initial_guess = declared_input_fields.get("initial_guess", {})
        energy_variable = shared_propulsion_energy["canonical_field"]
        output_data = {
            "schema_version": SCHEMA_VERSION,
            "schema_id": SCHEMA_ID,
            "project_name": args.project_name,
            "timestamp": generated_at,
            "numerical_converged": result.numerical_converged,
            "engineering_feasible": False,
            "stage_status": stage_status,
            "constraints": list(result.constraints),
            "provenance": {
                "workflow": "aircraft_design.class2_preliminary.run_sizing",
                "workflow_version": "2.0.0",
                "skill_version": "2.0",
                "formula_contract_version": "2.0.0",
                "schema_version": SCHEMA_VERSION,
                "generated_at": generated_at,
                "input_file": str(args.input_file.resolve()),
                "solver": {
                    "class1": "fixed-point weight closure with structural/system buildup",
                    "tolerance": solver_options.get("tolerance", 1e-3),
                    "max_iterations": solver_options.get("max_iter", 50),
                    "optimization_seed": int(solver_options.get("optimization_seed", 0)),
                },
                "propulsion_energy": shared_propulsion_energy,
                "input_fields": {
                    "requirements": _input_provenance(
                        asdict(req),
                        provided_req,
                        req_defaults,
                        declared_requirements,
                    ),
                    "initial_guess": _input_provenance(
                        asdict(guess),
                        guess_data,
                        guess_defaults,
                        declared_initial_guess,
                    ),
                },
                "models": [
                    "Class I structural and systems buildup",
                    "Propulsion-type-specific Breguet fuel closure and range inversion",
                    "Numerical takeoff/landing distance",
                    "Altitude-lapsed advanced propulsion",
                    "Segment mission fuel analysis",
                ],
                "uncertainty": {
                    "enabled": req.uncertainty_enabled,
                    "method": "deterministic three-case envelope",
                    "case_deltas": {
                        "nominal": {"cd0": 0.0, energy_variable: 0.0, "payload_kg": 0.0},
                        "optimistic": {"cd0": -0.05, energy_variable: -0.05, "payload_kg": -0.05},
                        "conservative": {"cd0": 0.10, energy_variable: 0.10, "payload_kg": 0.10},
                    },
                },
                "user_provenance": user_provenance,
            },
            "inputs": {
                "requirements": asdict(req),
                "initial_guess": asdict(guess),
                "propulsion": propulsion_model_to_input(shared_propulsion_model),
                "solver_options": solver_options,
            },
            "iteration_history": result.iteration_history,
            "design_adjustments": result.design_adjustments,
            "design_point": result.design_point,
            "advanced_results": {},
            "uncertainty_analysis": {},
            "outputs": {
                "converged": result.converged,
                "numerical_converged": result.numerical_converged,
                "engineering_feasible": False,
                "mtow_kg": result.mtow_kg,
                "empty_weight_kg": result.empty_weight_kg,
                "fuel_weight_kg": result.fuel_weight_kg,
                "wing_area_m2": result.wing_area_m2,
                "thrust_sl_n": result.thrust_sl_n,
                "geometry": result.geometry,
                "weight_breakdown": result.weight_breakdown,
                "performance": {
                    "actual_range_m": result.actual_range_m,
                    "takeoff_distance_m": result.takeoff_distance_m,
                    "landing_distance_m": result.landing_distance_m,
                    "values_are_predictions": True,
                },
                "iterations": result.iterations,
                "iteration_history": result.iteration_history,
                "design_adjustments": result.design_adjustments,
                "design_point": result.design_point,
                "drag_params": result.drag_params,
                "aero_params": result.aero_params,
                "propulsion_energy": shared_propulsion_energy,
                "advanced_results": {},
                "uncertainty_analysis": {},
            },
        }
        _refresh_contract_status(output_data)

        json_path = run_dir / "design_data.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {json_path}")

        reporter_v2 = ReportGeneratorV2(project_name=args.project_name)
        report_content_v2 = reporter_v2.generate_report(result, req)

        report_path_v2 = run_dir / "design_report_v2.md"
        with open(report_path_v2, "w", encoding="utf-8") as f:
            f.write(report_content_v2)
        print(f"Standard Report saved to {report_path_v2}")
        report_path = run_dir / "design_report.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content_v2)

        if result.converged and result.mtow_kg < 1e6:
            print("\n" + "=" * 60)
            print("  Stage 2: Extended Workflow (Detailed Geometry & Analysis)")
            print("=" * 60)

            inputs_for_geom = data.copy()
            if "requirements" not in inputs_for_geom:
                inputs_for_geom["requirements"] = asdict(req)
            if "initial_guess" not in inputs_for_geom:
                inputs_for_geom["initial_guess"] = asdict(guess)
            else:
                inputs_for_geom["initial_guess"] = dict(inputs_for_geom["initial_guess"])
            inputs_for_geom["initial_guess"]["thickness_ratio"] = result.geometry.get(
                "thickness_ratio", guess.thickness_ratio
            )

            detailed_geom = geometry_detailed_from_inputs(inputs_for_geom, result)
            result.geometry_detailed = detailed_geom
            output_data["stage_status"]["geometry"] = stage_record(
                "completed", blocking=True, message="Detailed parametric geometry was generated."
            )

            try:
                mesh_data = detailed_geom.generate_mesh()
                mesh_json_path = run_dir / "geometry_mesh.json"
                with open(mesh_json_path, "w", encoding="utf-8") as f:
                    json.dump(mesh_data, f, ensure_ascii=False)

                source_assets = Path(__file__).parent.parent.parent / "assets"
                dest_assets = run_dir / "assets"
                if source_assets.exists():
                    if dest_assets.exists():
                        shutil.rmtree(dest_assets)
                    shutil.copytree(source_assets, dest_assets)

                resource_config = {
                    "prefer_local": True,
                    "local_base_url": "assets",
                    "cdn_base_url": "https://unpkg.com/three@0.147.0",
                    "use_unminified": True,
                }

                html_path = run_dir / "geometry_3d.html"
                generate_three_view_html(mesh_data, str(html_path), resource_config=resource_config)
                mesh_parts = build_mesh_parts_from_geometry(mesh_data)
                if mesh_parts:
                    obj_path = run_dir / "geometry.obj"
                    with open(obj_path, "w", encoding="utf-8") as f:
                        f.write(mesh_to_obj(mesh_parts))
                    print(f"3D model OBJ saved to {obj_path}")
                print(f"3D mesh JSON saved to {mesh_json_path}")
                print(f"3D HTML preview saved to {html_path}")
            except Exception as e:
                print(f"3D model export failed: {e}")
                output_data["stage_status"]["visualization"] = stage_record(
                    "partial", blocking=False, message="Geometry completed, but one or more 3D preview artifacts failed.", error=str(e)
                )

            chart_gen = ChartDataGenerator(result, req)
            lift_data = chart_gen.generate_lift_curve()
            drag_data = chart_gen.generate_drag_polar()
            thrust_data = chart_gen.generate_thrust_curves()
            envelope_data = chart_gen.generate_flight_envelope()
            vn_data = chart_gen.generate_vn_diagram()
            plot_data_path = run_dir / "report_plot_data.json"
            plot_data = {
                "aero_cl_alpha": lift_data,
                "aero_drag_polar": drag_data,
                "perf_thrust_curves": thrust_data,
                "perf_flight_envelope": envelope_data,
                "struct_vn_diagram": vn_data,
            }
            with open(plot_data_path, "w", encoding="utf-8") as f:
                json.dump(plot_data, f, ensure_ascii=False)

            static_plotter = StaticPlotter(run_dir)
            plot_paths = {}

            plot_paths["lift_curve"] = str(static_plotter.plot_lift_curve(**lift_data))
            plot_paths["drag_polar"] = str(static_plotter.plot_drag_polar(**drag_data))
            plot_paths["thrust_curve"] = str(static_plotter.plot_thrust_curves(**thrust_data))
            plot_paths["flight_envelope"] = str(static_plotter.plot_flight_envelope(**envelope_data))
            plot_paths["vn_diagram"] = str(static_plotter.plot_vn_diagram(**vn_data))

            interactive_plotter = InteractivePlotter(output_dir=str(run_dir))
            charts = [
                plot_payload_range(payload_kg=req.payload_kg, range_km=req.range_m / 1000.0),
                plot_weight_breakdown(result.weight_breakdown),
            ]
            interactive_plotter.generate_html_report(charts, filename="interactive_charts.html")

            geom_dict = {
                "fuselage": {
                    "length_m": detailed_geom.fuselage.length,
                    "diameter_m": detailed_geom.fuselage.diameter,
                    "x_m": 0.0,
                    "y_m": 0.0,
                },
                "wing": {
                    "s_ref_m2": detailed_geom.wing.area,
                    "aspect_ratio": detailed_geom.wing.aspect_ratio,
                    "taper_ratio": detailed_geom.wing.taper_ratio,
                    "sweep_deg": detailed_geom.wing.sweep_qc,
                    "x_m": detailed_geom.wing.x_le_root,
                    "y_m": detailed_geom.wing.y_root,
                    "z_m": detailed_geom.wing.z_root,
                },
            }

            if detailed_geom.tail:
                s_wing = detailed_geom.wing.area
                s_ht = s_wing * detailed_geom.tail.area_ratio_to_wing * 0.75
                ar_ht = detailed_geom.tail.ht_aspect_ratio
                geom_dict["horizontal_tail"] = {
                    "s_ref_m2": s_ht,
                    "aspect_ratio": ar_ht,
                    "taper_ratio": 0.5,
                    "sweep_deg": 10.0,
                    "x_m": detailed_geom.fuselage.length * 0.85,
                }
                s_vt = s_wing * detailed_geom.tail.area_ratio_to_wing * 0.25
                ar_vt = detailed_geom.tail.vt_aspect_ratio
                geom_dict["vertical_tail"] = {
                    "s_ref_m2": s_vt,
                    "aspect_ratio": ar_vt,
                    "taper_ratio": 0.6,
                    "sweep_deg": 20.0,
                    "x_m": detailed_geom.fuselage.length * 0.85,
                    "z_m": detailed_geom.fuselage.diameter / 2.0,
                }

            view_paths = static_plotter.plot_3view(geom_dict)
            plot_paths.update(view_paths)

            vsp_script_path = run_dir / "model.vspscript"
            obj_path = run_dir / "model.obj"
            write_openvsp_script(
                geom=detailed_geom,
                s_ref_m2=result.wing_area_m2,
                out_path=vsp_script_path,
                include_visualization=True,
                export_obj_path=obj_path,
            )
            print(f"OpenVSP script saved to {vsp_script_path}")
            print(f"OBJ Export instruction added (target: {obj_path})")

            reporter_ext = ReportGeneratorExtended(project_name=args.project_name)

            plot_filenames = {k: Path(p).name for k, p in plot_paths.items()}

            report_content_ext = reporter_ext.generate_report(result, req, plot_filenames)

            report_path_ext = run_dir / "technical_roadmap_report.md"
            with open(report_path_ext, "w", encoding="utf-8") as f:
                f.write(report_content_ext)
            print(f"Technical Roadmap Report saved to {report_path_ext}")

            adv_viz = AdvancedVisualizer(run_dir)
            viz_script = adv_viz.create_visualization_script(obj_path)
            print(f"Advanced visualization script created: {viz_script}")

            if not args.no_viz:
                pass

            advanced_payload: dict = {}
            try:
                atm_cruise = isa_tropopause(req.cruise_altitude_m)
                v_cruise = req.cruise_mach * atm_cruise.a_m_s

                q_cruise = 0.5 * atm_cruise.rho_kg_m3 * v_cruise**2
                w_cruise_n = result.mtow_kg * CONST.g0_m_s2
                cl_cruise_calc = w_cruise_n / max(q_cruise * result.wing_area_m2, 1e-6)

                design_input = {
                    "cruise_altitude_m": req.cruise_altitude_m,
                    "cruise_speed_m_s": v_cruise,
                    "mtow_kg": result.mtow_kg,
                    "cl_cruise": cl_cruise_calc,
                }
                systems_config = data.get("systems", {}) if isinstance(data.get("systems", {}), dict) else {}
                try:
                    systems_obj = estimate_system_weights(
                        mtow_kg=result.mtow_kg,
                        n_limit=req.max_load_factor,
                        geometry=detailed_geom,
                        v_dive_m_s=v_cruise * 1.25,
                        payload_kg=req.payload_kg,
                        fuel_kg=result.fuel_weight_kg,
                        systems_config=systems_config,
                        s_ref_m2=result.wing_area_m2,
                    )
                    output_data["outputs"]["systems"] = systems_obj.to_dict()
                except Exception as e:
                    print(f"System weight estimation failed: {e}")
                    output_data["stage_status"]["systems"] = stage_record(
                        "partial", blocking=False, message="System-weight estimate was unavailable.", error=str(e)
                    )
                sea_level = isa_tropopause(0.0)
                wing_loading_pa = result.mtow_kg * CONST.g0_m_s2 / max(result.wing_area_m2, 1e-6)
                cl_max_assumed = req.cl_max_landing
                v_stall_m_s = (2.0 * wing_loading_pa / max(sea_level.rho_kg_m3 * cl_max_assumed, 1e-6)) ** 0.5
                mission_input = {
                    "range_m": req.range_m,
                    "cruise_altitude_m": req.cruise_altitude_m,
                    "cruise_speed_m_s": v_cruise,
                    "v_stall_m_s": v_stall_m_s,
                    "assumed_climb_rate_m_s": req.assumed_climb_rate_m_s,
                    "reserve_fraction": req.reserve_fraction,
                    "segments": [
                        {"type": "taxi", "time_s": 600},
                        {"type": "takeoff", "distance_m": req.takeoff_distance_m},
                        {"type": "climb", "altitude_m": req.cruise_altitude_m},
                        {"type": "cruise", "speed_m_s": v_cruise, "distance_m": req.range_m * 0.8},
                        {"type": "descent", "altitude_m": 0.0},
                        {"type": "landing", "distance_m": req.landing_distance_m},
                    ],
                }
                propulsion_input = propulsion_model_to_input(shared_propulsion_model)
                propulsion_input["thrust_sl_n"] = result.thrust_sl_n
                if req.propulsion_type == "jet":
                    propulsion_input.setdefault("bypass_ratio", 0.5)
                geometry_input = {
                    "s_ref_m2": result.wing_area_m2,
                    "b_m": result.geometry.get("span_m", (result.wing_area_m2 * guess.aspect_ratio) ** 0.5),
                    "cbar_m": result.geometry.get(
                        "mean_chord_m", result.wing_area_m2 / max(result.geometry.get("span_m", 1.0), 1e-6)
                    ),
                    "wing_t_c": result.geometry.get("thickness_ratio", guess.thickness_ratio),
                    "fuselage_length_m": result.geometry.get(
                        "fuselage_length_m", (result.geometry.get("span_m", 10.0) * 0.8)
                    ),
                    "fuselage_diameter_m": result.geometry.get("fuselage_diameter_m", 1.2),
                    "sweep_quarter_chord_deg": guess.sweep_deg,
                    "aspect_ratio": guess.aspect_ratio,
                    "taper_ratio": guess.taper_ratio,
                }
                stability_input = {
                    "x_ac_w_cbar": 0.25,
                    "x_cg_cbar": guess.cg_fraction_cbar,
                    "vh_coeff": guess.horizontal_tail_volume_coefficient,
                    "vv_coeff": 0.07,
                    "l_ht_m": geometry_input["fuselage_length_m"] * 0.45,
                    "l_vt_m": geometry_input["fuselage_length_m"] * 0.45,
                    "z_ht_m": 0.5,
                }
                structures_input = {
                    "n_limit": req.max_load_factor,
                    "ultimate_factor": 1.5,
                    "sigma_allow_pa": 250e6,
                    "density_kg_m3": 2700.0,
                    "relief_factor": 0.8,
                }
                baseline_design = {
                    "wing_loading_pa": wing_loading_pa,
                    "thrust_to_weight": result.design_point.get("thrust_to_weight", guess.thrust_to_weight),
                    "aspect_ratio": guess.aspect_ratio,
                    "cd0": guess.cd0,
                    energy_variable: shared_propulsion_energy["value"],
                    "range_m": req.range_m,
                    "payload_kg": req.payload_kg,
                }
                obstacle_height_m = req.obstacle_height_m
                if obstacle_height_m is None:
                    obstacle_height_m = 2.0 if req.takeoff_distance_m < 200.0 else 15.24
                empty_fraction = result.empty_weight_kg / max(result.mtow_kg, 1e-9)
                available_mission_fraction = result.fuel_weight_kg / (
                    max(result.mtow_kg, 1e-9) * (1.0 + req.reserve_fraction)
                )

                def evaluate_candidate(candidate: dict) -> dict:
                    ws = float(candidate["wing_loading_pa"])
                    tw = float(candidate["thrust_to_weight"])
                    ar = float(candidate["aspect_ratio"])
                    cd0 = float(candidate["cd0"])
                    energy_value = float(candidate[energy_variable])
                    mission_range = float(candidate["range_m"])
                    payload = float(candidate["payload_kg"])
                    candidate_area = result.mtow_kg * CONST.g0_m_s2 / max(ws, 1e-9)
                    cl = (0.9 * result.mtow_kg * CONST.g0_m_s2) / max(q_cruise * candidate_area, 1e-9)
                    candidate_polar = AeroPolar(cd0=cd0, e=guess.oswald_e, ar=ar)
                    cd = candidate_polar.cd(cl)
                    lift_to_drag = cl / max(cd, 1e-12)
                    candidate_propulsion = with_specific_fuel_consumption(
                        shared_propulsion_model,
                        energy_value,
                    )
                    predicted_range = cruise_range_from_fuel_fraction_m(
                        candidate_propulsion,
                        fuel_fraction=available_mission_fraction,
                        cruise_speed_m_s=v_cruise,
                        lift_to_drag=lift_to_drag,
                    )
                    if predicted_range is None:
                        predicted_range = 0.0
                    takeoff_distance = takeoff_distance_over_obstacle_m(
                        wing_loading_pa=ws,
                        rho_kg_m3=sea_level.rho_kg_m3,
                        cl_max_takeoff=req.cl_max_takeoff,
                        thrust_to_weight=tw,
                        obstacle_height_m=obstacle_height_m,
                        climb_gradient=req.takeoff_climb_gradient,
                        runway_slope=req.runway_slope,
                        headwind_m_s=req.headwind_m_s,
                    )
                    landing_distance = landing_distance_over_obstacle_m(
                        wing_loading_pa=ws,
                        rho_kg_m3=sea_level.rho_kg_m3,
                        cl_max_landing=req.cl_max_landing,
                        obstacle_height_m=obstacle_height_m,
                        approach_angle_deg=req.landing_approach_angle_deg,
                        decel_g=req.landing_decel_g,
                        runway_slope=req.runway_slope,
                        headwind_m_s=req.headwind_m_s,
                    )
                    required_fuel_fraction = cruise_fuel_fraction(
                        candidate_propulsion,
                        range_m=mission_range,
                        cruise_speed_m_s=v_cruise,
                        lift_to_drag=lift_to_drag,
                    ) * (
                        1.0 + req.reserve_fraction
                    )
                    closure_denominator = 1.0 - empty_fraction - required_fuel_fraction
                    estimated_mtow = payload / closure_denominator if closure_denominator > 1e-6 else None
                    feasible = (
                        predicted_range + max(1.0, mission_range * 1e-9) >= mission_range
                        and takeoff_distance <= req.takeoff_distance_m + 1e-6
                        and landing_distance <= req.landing_distance_m + 1e-6
                        and estimated_mtow is not None
                    )
                    return {
                        "estimated_mtow_kg": estimated_mtow,
                        "predicted_range_m": predicted_range,
                        "takeoff_distance_m": takeoff_distance if math.isfinite(takeoff_distance) else None,
                        "landing_distance_m": landing_distance if math.isfinite(landing_distance) else None,
                        "lift_to_drag": lift_to_drag,
                        "required_fuel_fraction": required_fuel_fraction,
                        "feasible": feasible,
                        "screening_passed": feasible,
                        "evaluation_scope": "reduced_order_screening",
                        "engineering_revalidation_performed": False,
                        "propulsion_energy": propulsion_energy_metadata(candidate_propulsion),
                    }

                if req.uncertainty_enabled:
                    uncertainty_case_deltas = output_data["provenance"]["uncertainty"]["case_deltas"]
                    uncertainty_cases = []
                    for case_name in ("nominal", "optimistic", "conservative"):
                        deltas = uncertainty_case_deltas[case_name]
                        case_design = baseline_design.copy()
                        for variable, delta_ratio in deltas.items():
                            case_design[variable] = baseline_design[variable] * (1.0 + delta_ratio)
                        uncertainty_cases.append(
                            {
                                "id": case_name,
                                "deltas": deltas,
                                "design_point": case_design,
                                "metrics": evaluate_candidate(case_design),
                            }
                        )
                    uncertainty_analysis = {
                        "method": "deterministic three-case envelope",
                        "variables": ["cd0", energy_variable, "payload_kg"],
                        "cases": uncertainty_cases,
                    }
                    output_data["uncertainty_analysis"] = uncertainty_analysis
                    output_data["outputs"]["uncertainty_analysis"] = uncertainty_analysis
                    output_data["stage_status"]["uncertainty"] = stage_record(
                        "completed",
                        blocking=False,
                        message="Nominal, optimistic, and conservative uncertainty cases completed.",
                    )
                    output_data["constraints"].append(
                        normalized_constraint(
                            constraint_id="uncertainty.robust_cases",
                            label="Feasible deterministic uncertainty cases",
                            category="uncertainty",
                            direction="minimum",
                            required=3.0,
                            actual=float(sum(case["metrics"]["feasible"] for case in uncertainty_cases)),
                            unit="count",
                            blocking=False,
                            evidence={
                                "model": "Deterministic nominal/optimistic/conservative envelope",
                                "prediction": True,
                                "case_deltas": uncertainty_case_deltas,
                            },
                            recommendation="Review conservative CD0, SFC, and payload margins before freezing the design.",
                        )
                    )

                def bounds(value: float, lower_floor: float = 1e-9) -> list[float]:
                    return [max(lower_floor, value * 0.9), max(lower_floor, value * 1.1)]

                optimization_input = {
                    "design_variables": {
                        "wing_loading_pa": bounds(baseline_design["wing_loading_pa"], 100.0),
                        "thrust_to_weight": bounds(baseline_design["thrust_to_weight"], 0.01),
                        "aspect_ratio": bounds(baseline_design["aspect_ratio"], 1.0),
                        "cd0": bounds(baseline_design["cd0"], 0.001),
                        energy_variable: bounds(baseline_design[energy_variable], 1e-10),
                        "range_m": bounds(baseline_design["range_m"], 1.0),
                        "payload_kg": bounds(baseline_design["payload_kg"], 0.0),
                    },
                    "constraints": {
                        "takeoff": lambda d: evaluate_candidate(d)["takeoff_distance_m"] is not None
                        and evaluate_candidate(d)["takeoff_distance_m"] <= req.takeoff_distance_m,
                        "landing": lambda d: evaluate_candidate(d)["landing_distance_m"] is not None
                        and evaluate_candidate(d)["landing_distance_m"] <= req.landing_distance_m,
                        "range": lambda d: evaluate_candidate(d)["predicted_range_m"]
                        + max(1.0, float(d["range_m"]) * 1e-9)
                        >= d["range_m"],
                    },
                    "objective": "estimated_mtow_kg",
                    "objective_direction": "minimize",
                    "n_iterations": int(solver_options.get("optimization_iterations", 50)),
                    "seed": int(solver_options.get("optimization_seed", 0)),
                    "baseline_design": baseline_design,
                    "evaluation_func": evaluate_candidate,
                }
                adv_result = execute_advanced_design(
                    design_input=design_input,
                    mission_input=mission_input,
                    propulsion_input=propulsion_input,
                    geometry_input=geometry_input,
                    stability_input=stability_input,
                    structures_input=structures_input,
                    optimization_input=optimization_input,
                    isa_delta_c=req.isa_delta_c,
                )
                advanced_payload = {
                    "stage2_aero": vars(adv_result.stage2_aero),
                    "stage3_propulsion": vars(adv_result.stage3_propulsion),
                    "stage4_mission": vars(adv_result.stage4_mission),
                    "stage5_stability": vars(adv_result.stage5_stability),
                    "stage6_structures": vars(adv_result.stage6_structures),
                    "stage7_optimization": (
                        vars(adv_result.stage7_optimization) if adv_result.stage7_optimization else None
                    ),
                }
                for stage_id, label in (
                    ("stage2_aero", "Aerodynamic buildup completed."),
                    ("stage3_propulsion", "Installed propulsion checks completed."),
                    ("stage4_mission", "Segment mission analysis completed."),
                    ("stage5_stability", "Static stability and trim screening completed."),
                    ("stage6_structures", "Structural loads and weight feedback completed."),
                ):
                    output_data["stage_status"][stage_id] = stage_record("completed", blocking=True, message=label)
                if adv_result.stage7_optimization is None:
                    output_data["stage_status"]["stage7_optimization"] = stage_record(
                        "skipped", blocking=False, message="Candidate exploration was not requested."
                    )
                elif adv_result.stage7_optimization.feasible_designs:
                    output_data["stage_status"]["stage7_optimization"] = stage_record(
                        "completed",
                        blocking=False,
                        message="Seeded reduced-order screening and OAT sensitivity completed.",
                    )
                else:
                    output_data["stage_status"]["stage7_optimization"] = stage_record(
                        "partial",
                        blocking=False,
                        message="OAT sensitivity completed, but no candidate passed reduced-order screening.",
                    )
                constraint_reqs = {
                    "fuel_weight_kg": result.fuel_weight_kg,
                    "aircraft_role": req.aircraft_role,
                }
                if isinstance(inputs_for_geom.get("geometry_constraints", None), dict):
                    constraint_reqs.update(inputs_for_geom["geometry_constraints"])
                geom_constraints = GeometryConstraintChecker(
                    detailed_geom.wing,
                    detailed_geom.fuselage,
                    constraint_reqs,
                ).check_all()
                advanced_payload["geometry_constraints"] = [vars(c) for c in geom_constraints]
                vspaero_data = {"enabled": False}
                if shutil.which("vspaero"):
                    try:
                        aircraft_geom = parametric_to_aircraft_geometry(detailed_geom)
                        vspaero_output = run_dir / "vspaero_output.txt"
                        vspaero_input = run_dir / "vspaero_input.txt"
                        vsp_res = run_vspaero_analysis(
                            geometry=aircraft_geom,
                            mach=req.cruise_mach,
                            alpha_deg=0.0,
                            output_file=str(vspaero_output),
                            input_file=str(vspaero_input),
                        )
                        vspaero_data = {
                            "enabled": True,
                            "input_file": str(vspaero_input),
                            "output_file": str(vspaero_output),
                            "result": vars(vsp_res),
                        }
                    except Exception as vspaero_error:
                        vspaero_data = {"enabled": True, "error": str(vspaero_error)}
                        output_data["stage_status"]["vspaero"] = stage_record(
                            "failed", blocking=False, message="Optional VSPAERO execution failed.", error=str(vspaero_error)
                        )
                advanced_payload["vspaero"] = vspaero_data
                adv_json = run_dir / f"advanced_design_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(adv_json, "w", encoding="utf-8") as f:
                    json.dump(advanced_payload, f, indent=2, ensure_ascii=False)
                print(f"Advanced design results saved to {adv_json}")
                adv_report = run_dir / "advanced_design_report.md"
                try:
                    generate_advanced_design_report(str(adv_json), str(adv_report))
                except Exception as report_error:
                    print(f"Advanced report generation failed: {report_error}")
                    output_data["stage_status"]["reporting"] = stage_record(
                        "partial", blocking=False, message="Advanced calculations completed, but report generation failed.", error=str(report_error)
                    )
            except AdvancedDesignStageError as stage_error:
                print(f"Advanced design execution failed: {stage_error}")
                import traceback
                traceback.print_exc()

                advanced_payload = {
                    stage_id: vars(stage_result)
                    for stage_id, stage_result in stage_error.partial_results.items()
                }
                advanced_payload["failure"] = {
                    "stage_id": stage_error.stage_id,
                    "error": str(stage_error.cause),
                    "partial_results_preserved": sorted(stage_error.partial_results),
                }
                advanced_stage_order = (
                    "stage2_aero",
                    "stage3_propulsion",
                    "stage4_mission",
                    "stage5_stability",
                    "stage6_structures",
                    "stage7_optimization",
                )
                failed_index = advanced_stage_order.index(stage_error.stage_id)
                for index, stage_id in enumerate(advanced_stage_order):
                    blocking = stage_id != "stage7_optimization"
                    if stage_id in stage_error.partial_results:
                        output_data["stage_status"][stage_id] = stage_record(
                            "completed",
                            blocking=blocking,
                            message="Stage completed before a downstream advanced-design failure.",
                        )
                    elif index == failed_index:
                        output_data["stage_status"][stage_id] = stage_record(
                            "failed",
                            blocking=blocking,
                            message=f"Advanced workflow failed during {stage_id}.",
                            error=str(stage_error.cause),
                        )
                    else:
                        output_data["stage_status"][stage_id] = stage_record(
                            "skipped",
                            blocking=blocking,
                            message=f"Skipped because {stage_error.stage_id} failed upstream.",
                        )
                partial_path = run_dir / "advanced_design_partial.json"
                with open(partial_path, "w", encoding="utf-8") as f:
                    json.dump(advanced_payload, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"Advanced design execution failed: {e}")
                import traceback
                traceback.print_exc()

                if advanced_payload:
                    output_data["stage_status"]["reporting"] = stage_record(
                        "partial", blocking=False, message="Advanced calculations completed, but an artifact step failed.", error=str(e)
                    )
                else:
                    output_data["stage_status"]["stage2_aero"] = stage_record(
                        "failed", blocking=True, message="Advanced workflow failed before producing canonical results.", error=str(e)
                    )
                    for stage_id in ("stage3_propulsion", "stage4_mission", "stage5_stability", "stage6_structures"):
                        output_data["stage_status"][stage_id] = stage_record(
                            "skipped", blocking=True, message="Skipped because an upstream advanced stage failed."
                        )
                    output_data["stage_status"]["stage7_optimization"] = stage_record(
                        "skipped", blocking=False, message="Skipped because the advanced workflow failed."
                    )

            if advanced_payload:
                output_data["advanced_results"] = advanced_payload
                output_data["outputs"]["advanced_results"] = advanced_payload
                output_data["constraints"].extend(
                    normalized_advanced_constraints(
                        advanced_payload,
                        available_fuel_kg=result.fuel_weight_kg,
                        class1_structure_kg=float(result.weight_breakdown.get("structure", 0.0)),
                    )
                )

        else:
            print("\nSkipping Extended Workflow (Analysis not converged or invalid).")

        _refresh_contract_status(output_data)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        unified_reporter = UnifiedReportGenerator(project_name=args.project_name)
        unified_report_md, unified_report_json = unified_reporter.generate_report(output_data, run_dir)
        unified_report_path = run_dir / "design_report_unified.md"
        with open(unified_report_path, "w", encoding="utf-8") as f:
            f.write(unified_report_md)
        unified_json_path = run_dir / "design_report_unified.json"
        with open(unified_json_path, "w", encoding="utf-8") as f:
            json.dump(unified_report_json, f, ensure_ascii=False, indent=2)
        print(f"Unified Report saved to {unified_report_path}")

        send_report_path_to_gui(run_dir)

        if output_data.get("engineering_feasible") is True:
            print("\nSuccess: numerical convergence and all blocking engineering gates passed.")
        else:
            failed_ids = [
                str(item.get("id"))
                for item in output_data.get("constraints", [])
                if isinstance(item, dict)
                and item.get("blocking") is True
                and item.get("passed") is not True
            ]
            print(
                "\nDesign completed but is not deliverable. Failed blocking checks: "
                + (", ".join(failed_ids) if failed_ids else "incomplete engineering evidence")
            )
            sys.exit(2)

    except Exception as e:
        print(f"Error during sizing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        if log_file:
            log_file.flush()
            log_file.close()
        sys.stdout = original_stdout
        sys.stderr = original_stderr


if __name__ == "__main__":
    main()
