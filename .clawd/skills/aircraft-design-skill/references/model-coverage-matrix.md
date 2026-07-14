# Model Coverage Matrix

This is a readable snapshot of `src/design_intake/coverage.py`. The runtime registry is authoritative. Coverage means the current model can evaluate the field inside its stated envelope; it does not guarantee that a candidate will pass.

## Semantics

| Status | Interpretation | Solver action |
| --- | --- | --- |
| `covered` | A registered deterministic model evaluates the field in its applicable envelope. | Continue to consistency checks and solving. |
| `partial` | The field is revalidated or approximated, but is not a complete direct model or optimizer constraint. | Keep visible, explain limitation and apply the final hard gate. |
| `unsupported` | No registered applicable model exists, or the value is outside the registered envelope. | Block mandatory requirements and report a model gap. Never infer physical infeasibility. |

Unknown fields fail closed as `unsupported`. A locked field or any unsupported non-soft field is blocking. An unsupported, unlocked `soft_goal` may be non-blocking, but remains in the intent and final report.

## Covered fields

All fields below use model ID `aircraft_class_i_ii_v2`.

| Canonical key | Coverage or envelope |
| --- | --- |
| `range_m` | User-prescribed total mission distance used for Class I/II segment synthesis, fuel demand and capacity closure. The returned segment-distance sum is an evaluated mission distance, not an independent maximum-range prediction. |
| `payload_kg` | Mass and mission closure. |
| `cruise_mach` | Subsonic cruise aero and propulsion evaluation, envelope 0.03 to 0.85. |
| `cruise_altitude_m` | Atmosphere, drag, thrust and mission evaluation, envelope 0 to 35000 m. |
| `takeoff_distance_m` | Predicted takeoff-distance hard gate. |
| `landing_distance_m` | Predicted landing-distance hard gate. |
| `max_load_factor` | Structural design-load input. |
| `sustained_turn_g` | Sustained-turn thrust constraint. |
| `service_ceiling_m` | Service-ceiling thrust constraint. |
| `aircraft_role` | Task-class selection and reporting. |
| `propulsion_type` | Generic propulsion branch, allowed values `jet` and `prop`. |
| `reserve_fraction` | Mission fuel reserve hard gate. |
| `tail_layout` | Parametric tail branch, allowed values `conventional`, `t_tail`, `v_tail`, `twin_fin`. |
| `cl_max_takeoff`, `cl_max_landing` | High-lift technology assumptions used by field constraints. |
| `assumed_climb_rate_m_s` | Climb and ceiling assumption. |
| `uncertainty_enabled` | Implemented uncertainty-analysis switch. |
| `mtow_kg` | Class I weight-loop initial design variable. |
| `wing_loading_pa`, `thrust_to_weight` | Constraint-analysis design variables. |
| `aspect_ratio`, `sweep_deg`, `taper_ratio`, `thickness_ratio` | Parametric wing geometry inputs. |
| `jet_tsfc_kg_per_n_s`, `prop_bsfc_kg_per_j`, `prop_efficiency` | Generic propulsion technology assumptions. |
| `cd0`, `oswald_e` | Class I/II drag-polar technology assumptions. |
| `cg_fraction_cbar` | Longitudinal static-margin input. |
| `horizontal_tail_volume_coefficient` | Preliminary tail-sizing input. |

Cruise conditions above Mach 0.85 are outside this registry because the current workflow does not close transonic drag rise, propulsion matching, heating, flutter or aeroelastic effects. Treat them as a model-applicability gap, not as physical infeasibility.

## Partial fields

| Canonical key | Limitation |
| --- | --- |
| `sfc_cruise_1_s` | Legacy energy input is migrated at the declared cruise condition. |
| `max_mtow_kg` | Revalidated after weight closure; not yet a direct optimizer constraint. |
| `max_aspect_ratio` | Revalidated after geometry closure and honored by bounded repair. |

Do not silently downgrade partial hard requirements to advisory outputs. Their final gate still has to pass for preliminary feasibility.

## Unsupported fields

| Canonical key | Missing validation chain |
| --- | --- |
| `max_flight_mach` | Maximum-speed, drag-rise, propulsion-limit and flutter validation. |
| `launch_mode` | Launch trajectory and launch-load interface. |
| `launch_field_altitude_m` | Launch-site atmosphere coupled to launch trajectory. |
| `booster_end_mach` | Rocket-booster separation trajectory. |
| `booster_end_relative_altitude_m` | Rocket-booster separation altitude. |
| `recovery_mode` | Recovery deployment and aircraft-load interface. |
| `parachute_open_mach` | Parachute deployment envelope and opening shock. |
| `parachute_open_relative_altitude_m` | Parachute descent and altitude margin. |
| `engine_count` | Engine count, installation and integration validation. |
| `configuration_reference` | Reference styling converted into validated geometry constraints. |
| `stealth_requirement` | RCS, signature control, inlet/exhaust shielding and low-observable materials validation. |
| `min_cruise_endurance_s` | Independent maximum fuel-limited cruise-endurance prediction. The current segment mission only prescribes duration from mission distance. |

For example, a request that includes rocket assist and parachute recovery can still have a covered cruise subproblem. The overall request remains `unsupported` until those mandatory launch and recovery requirements gain models or the user explicitly accepts a reduced scope. A covered subproblem must not be labeled an overall feasible vehicle.

## Canonical aliases

The registry normalizes common intent paths:

```text
performance.max_mach -> max_flight_mach
performance.max_flight_mach -> max_flight_mach
launch.mode -> launch_mode
launch.field_altitude_m -> launch_field_altitude_m
launch.booster_end_mach -> booster_end_mach
launch.booster_end_relative_altitude_m -> booster_end_relative_altitude_m
recovery.mode -> recovery_mode
recovery.parachute_open_mach -> parachute_open_mach
recovery.parachute_open_relative_altitude_m -> parachute_open_relative_altitude_m
propulsion.engine_count -> engine_count
configuration.reference -> configuration_reference
configuration.stealth_requirement -> stealth_requirement
geometry.max_aspect_ratio -> max_aspect_ratio
performance.min_cruise_endurance_s -> min_cruise_endurance_s
weights.max_mtow_kg -> max_mtow_kg
```

When adding a user-visible requirement, add a deterministic coverage entry and regression test before presenting it as supported.
