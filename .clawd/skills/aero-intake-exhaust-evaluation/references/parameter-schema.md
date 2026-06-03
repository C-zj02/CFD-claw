# case.json 参数契约

`case.json` 是技能和外部工具之间的稳定数据合同。字段可以扩展，但不要改变已有字段含义。

## 顶层字段

```json
{
  "case_id": "intake-demo-001",
  "run_mode": "dry_run",
  "analysis_type": "intake_duct",
  "fidelity": "quick",
  "toolchain": {
    "preferred_tool": "openfoam",
    "candidate_tools": ["starccm", "openfoam", "matlab"],
    "execute_command": null
  },
  "geometry": {},
  "flow_conditions": {},
  "boundary_conditions": {},
  "mesh": {},
  "solver": {},
  "monitoring": {},
  "postprocessing": {},
  "custom_variables": [],
  "outputs": {},
  "confirmation_log": [],
  "assumptions": []
}
```

## 字段说明

- `case_id`：结果目录和文件名使用的稳定 ID，只用字母、数字、下划线、短横线。
- `run_mode`：`dry_run`、`mock`、`execute`。
- `analysis_type`：`external_aero`、`intake_duct`、`nozzle_exhaust`、`coupled_propulsion`、`postprocess_only`。
- `fidelity`：`quick`、`high`、`custom`。
- `toolchain.preferred_tool`：`starccm`、`openfoam`、`matlab`、`custom`、`all`。
- `confirmation_log`：记录用户确认或工程默认，例如 `{ "node": "boundary_naming", "status": "pending", "note": "AIP face not named" }`。
- `assumptions`：默认值和假设列表。每条应包含 `field`、`value`、`source`、`reason`。

## geometry

```json
{
  "files": [{"path": "models/intake.step", "role": "main_geometry", "format": "step"}],
  "unit": "m",
  "coordinate_system": {
    "x_axis": "downstream",
    "y_axis": "right",
    "z_axis": "up"
  },
  "reference_values": {
    "area_ref_m2": null,
    "length_ref_m": null,
    "moment_center_m": [0, 0, 0]
  },
  "boundary_names": {
    "farfield": [],
    "walls": [],
    "inlets": [],
    "outlets": [],
    "symmetry": [],
    "aip": [],
    "nozzle_inlet": [],
    "nozzle_throat": [],
    "nozzle_exit": []
  }
}
```

## flow_conditions

```json
{
  "mach": 0.8,
  "altitude_m": 10000,
  "alpha_deg": 0,
  "beta_deg": 0,
  "temperature_k": null,
  "pressure_pa": null,
  "reynolds_number": null,
  "gas_model": "ideal_air"
}
```

## boundary_conditions

```json
{
  "farfield": {"type": "pressure_farfield", "mach": 0.8},
  "walls": {"type": "no_slip_adiabatic"},
  "inlet": {"type": "mass_flow_or_total_conditions", "value": null},
  "outlet": {"type": "pressure_outlet", "static_pressure_pa": null},
  "aip": {"type": "monitor_plane"},
  "nozzle_exit": {"type": "pressure_outlet_or_supersonic_outlet"}
}
```

## mesh

```json
{
  "target_cell_count": 1000000,
  "mesh_level": "coarse",
  "boundary_layer": {
    "enabled": true,
    "layers": 8,
    "growth_rate": 1.25,
    "target_y_plus": 30
  },
  "refinement_regions": [
    {"name": "lip", "type": "surface", "target_size_m": null, "reason": "intake lip separation risk"}
  ]
}
```

## solver

```json
{
  "steady": true,
  "compressible": true,
  "turbulence_model": "SST k-omega",
  "iterations": 1000,
  "cfl": 5,
  "convergence_criteria": {
    "residual_target": 0.0001,
    "monitor_stability_window": 100
  },
  "numerics": {
    "initial_order": "first",
    "final_order": "second"
  }
}
```

## monitoring 和 postprocessing

```json
{
  "monitoring": {
    "residuals": ["continuity", "x_momentum", "y_momentum", "z_momentum", "energy"],
    "integrals": ["mass_flow", "force", "moment"],
    "custom_monitors": ["total_pressure_recovery"]
  },
  "postprocessing": {
    "metrics": ["CL", "CD", "total_pressure_recovery", "distortion", "gross_thrust"],
    "contours": ["mach", "static_pressure", "total_pressure", "wall_y_plus"],
    "slices": [{"name": "AIP", "boundary": "aip"}]
  }
}
```

