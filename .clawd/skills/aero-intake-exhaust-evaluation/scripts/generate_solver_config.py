#!/usr/bin/env python3
"""Generate draft solver configuration files for StarCCM+, OpenFOAM, and MATLAB."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_case(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("case file must contain a JSON object")
    return data


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def boundary_list(case: dict[str, Any], key: str) -> list[str]:
    value = case.get("geometry", {}).get("boundary_names", {}).get(key, [])
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    return []


def starccm_macro(case: dict[str, Any]) -> str:
    case_json = json.dumps(case, ensure_ascii=False, indent=2).replace("*/", "* /")
    solver = case.get("solver", {})
    mesh = case.get("mesh", {})
    return f"""// Auto-generated StarCCM+ macro draft.
// This file is a scaffold for dry-run review. Adapt API calls to the installed StarCCM+ version.

import star.common.*;

public class RunAeroEvaluation extends StarMacro {{
  public void execute() {{
    Simulation sim = getActiveSimulation();
    sim.println("Case ID: {case.get('case_id')}");
    sim.println("Analysis type: {case.get('analysis_type')}");
    sim.println("Run mode: {case.get('run_mode')}");
    sim.println("Turbulence model request: {solver.get('turbulence_model')}");
    sim.println("Target cell count: {mesh.get('target_cell_count')}");
    sim.println("TODO: import geometry, bind named boundaries, configure mesh, physics, reports, and scenes.");
  }}
}}

/*
Resolved case JSON:
{case_json}
*/
"""


def starccm_batch(case: dict[str, Any]) -> str:
    return f"""@echo off
REM Draft StarCCM+ batch command. Confirm installation path and license before execute mode.
REM starccm+ -batch run_starccm.java -np 8 {case.get('case_id')}.sim
echo Dry-run only: StarCCM+ command is not executed.
"""


def openfoam_control_dict(case: dict[str, Any]) -> str:
    solver = case.get("solver", {})
    iterations = solver.get("iterations", 1000)
    return f"""/* Auto-generated OpenFOAM controlDict draft. */
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      controlDict;
}}

application     rhoSimpleFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         {iterations};
deltaT          1;
writeControl    timeStep;
writeInterval   100;
purgeWrite      0;
writeFormat     ascii;
writePrecision  8;
runTimeModifiable true;
"""


def openfoam_fv_schemes() -> str:
    return """/* Auto-generated OpenFOAM fvSchemes draft. */
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      fvSchemes;
}

ddtSchemes
{
    default         steadyState;
}

gradSchemes
{
    default         Gauss linear;
}

divSchemes
{
    default         none;
    div(phi,U)      Gauss upwind;
    div(phi,e)      Gauss upwind;
    div(phi,k)      Gauss upwind;
    div(phi,omega)  Gauss upwind;
}

laplacianSchemes
{
    default         Gauss linear corrected;
}

interpolationSchemes
{
    default         linear;
}

snGradSchemes
{
    default         corrected;
}
"""


def openfoam_fv_solution(case: dict[str, Any]) -> str:
    residual = case.get("solver", {}).get("convergence_criteria", {}).get("residual_target", 1e-4)
    return f"""/* Auto-generated OpenFOAM fvSolution draft. */
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      fvSolution;
}}

solvers
{{
    "(rho|U|e|k|omega)"
    {{
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       {residual};
        relTol          0.1;
    }}

    p
    {{
        solver          GAMG;
        tolerance       {residual};
        relTol          0.1;
        smoother        GaussSeidel;
    }}
}}

SIMPLE
{{
    nNonOrthogonalCorrectors 0;
    residualControl
    {{
        p               {residual};
        U               {residual};
        e               {residual};
        k               {residual};
        omega           {residual};
    }}
}}

relaxationFactors
{{
    fields
    {{
        p               0.3;
        rho             0.5;
    }}
    equations
    {{
        U               0.7;
        e               0.7;
        k               0.7;
        omega           0.7;
    }}
}}
"""


def openfoam_readme(case: dict[str, Any]) -> str:
    boundaries = case.get("geometry", {}).get("boundary_names", {})
    boundary_lines = "\n".join(f"- {key}: {value}" for key, value in boundaries.items())
    return f"""# OpenFOAM Draft Case

Case ID: `{case.get('case_id')}`

This directory is a dry-run scaffold. It does not contain a mesh or complete boundary field files.

## Requested Boundaries

{boundary_lines}

## Next Steps Before Execute

1. Confirm OpenFOAM version and solver.
2. Generate or import mesh.
3. Map named boundaries to OpenFOAM patches.
4. Fill `0/` field files.
5. Run mesh quality checks before solver execution.
"""


def matlab_script(case: dict[str, Any]) -> str:
    metrics = case.get("postprocessing", {}).get("metrics", [])
    metric_lines = "\n".join(f"% - {metric}" for metric in metrics)
    return f"""% Auto-generated MATLAB post-processing scaffold.
% Case ID: {case.get('case_id')}
% Run mode: {case.get('run_mode')}

caseId = '{case.get('case_id')}';
runDir = fullfile(pwd, '..', 'run');
resultsDir = fullfile(pwd, '..', 'results');
if ~exist(resultsDir, 'dir')
    mkdir(resultsDir);
end

% Expected metrics:
{metric_lines}

monitorsPath = fullfile(runDir, 'monitors.csv');
if exist(monitorsPath, 'file')
    monitors = readtable(monitorsPath);
    writetable(monitors, fullfile(resultsDir, 'monitors_copy.csv'));
else
    warning('monitors.csv not found. Use mock_run.py or external solver output first.');
end

disp(['Post-processing scaffold completed for ', caseId]);
"""


def custom_adapter(case: dict[str, Any]) -> str:
    payload = {
        "tool_name": "custom_cfd_tool",
        "case_id": case.get("case_id"),
        "run_mode": case.get("run_mode"),
        "required_inputs": ["case.json", "geometry files", "mesh or meshing recipe"],
        "expected_outputs": ["residuals.csv", "monitors.csv", "metrics.csv", "solver.log"],
        "notes": "Fill this contract with customer-specific command, config format, and result file mapping.",
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def generate(case: dict[str, Any], output: Path, tools: list[str]) -> list[str]:
    written: list[str] = []
    output.mkdir(parents=True, exist_ok=True)
    resolved_case = output / "resolved_case.json"
    write_text(resolved_case, json.dumps(case, ensure_ascii=False, indent=2) + "\n")
    written.append(str(resolved_case))

    if "starccm" in tools:
        path = output / "starccm" / "run_starccm.java"
        write_text(path, starccm_macro(case))
        written.append(str(path))
        path = output / "starccm" / "run_starccm.bat"
        write_text(path, starccm_batch(case))
        written.append(str(path))

    if "openfoam" in tools:
        files = {
            output / "openfoam" / "system" / "controlDict": openfoam_control_dict(case),
            output / "openfoam" / "system" / "fvSchemes": openfoam_fv_schemes(),
            output / "openfoam" / "system" / "fvSolution": openfoam_fv_solution(case),
            output / "openfoam" / "system" / "decomposeParDict": "numberOfSubdomains 4;\nmethod scotch;\n",
            output / "openfoam" / "constant" / "transportProperties": "transportModel Newtonian;\n",
            output / "openfoam" / "README_OPENFOAM.md": openfoam_readme(case),
        }
        for path, text in files.items():
            write_text(path, text)
            written.append(str(path))

    if "matlab" in tools:
        path = output / "matlab" / "postprocess_case.m"
        write_text(path, matlab_script(case))
        written.append(str(path))

    if "custom" in tools:
        path = output / "custom" / "adapter_contract.json"
        write_text(path, custom_adapter(case))
        written.append(str(path))

    manifest = {"case_id": case.get("case_id"), "status": "generated", "files": written}
    path = output / "config_manifest.json"
    write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    written.append(str(path))
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="Path to case JSON")
    parser.add_argument("--tool", default="all", help="starccm, openfoam, matlab, custom, or all")
    parser.add_argument("--output", required=True, help="Output config directory")
    args = parser.parse_args()

    tool = args.tool.lower()
    tools = ["starccm", "openfoam", "matlab", "custom"] if tool == "all" else [tool]
    invalid = [item for item in tools if item not in {"starccm", "openfoam", "matlab", "custom"}]
    if invalid:
        raise SystemExit(f"unknown tool(s): {invalid}")

    written = generate(load_case(Path(args.case)), Path(args.output), tools)
    print(json.dumps({"status": "ok", "files": written}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
