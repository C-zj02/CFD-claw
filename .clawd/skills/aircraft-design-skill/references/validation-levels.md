# Validation Levels and Delivery Gates

## Principle

Numerical convergence, model coverage and engineering feasibility are separate claims. Always report them separately. A higher validation level requires evidence from every lower level plus its own gates.

## Lifecycle and result levels

| State | Minimum evidence | Allowed wording |
| --- | --- | --- |
| `diagnosis.ready_for_solver` | Inputs present, consistency checks pass and no blocking model gap. Explicit confirmation has not yet been implied. | "Preflight complete; awaiting baseline confirmation." |
| `confirmed=true, can_submit=true` | The exact current revision has a server-owned user confirmation and is eligible for one audited submission. | "Confirmed and ready for deterministic sizing submission." |
| `conceptually_feasible` | Implemented conceptual mission, mass and constraint screens pass for the stated scope. Assumptions and coverage are disclosed. | "Conceptually feasible under the stated low-fidelity assumptions." |
| `preliminary_feasible` | Full implemented Class I/II run completes, engineering gates below pass, and no mandatory requirement is unsupported. | "Preliminary design candidate within the implemented model scope." |
| `robust_preliminary_feasible` | Preliminary feasibility plus declared uncertainty or conservative margin checks pass. | "Robust preliminary candidate for the declared uncertainty set." |
| `infeasible` | Applicable models ran, bounded search was exhausted, and at least one covered hard constraint remains failed. | "No feasible candidate was found in the declared design space." |

Do not use `infeasible` for `unsupported`, missing inputs, dependency errors, timeouts or numerical failures.

`nonconverged` is a numerical diagnosis. Its last iterate cannot justify a hard-requirement relaxation. Only a numerically converged engineering failure with complete blocking-constraint evidence may enter the `infeasible` trade path.

## Preliminary delivery gate

Call a result `preliminary_feasible` only when all of the following are true:

The compact machine gate first requires all three values exactly:

```text
engineering.numerical_converged === true
engineering.engineering_feasible === true
engineering.blocking_failed_count === 0
```

If any compact field is missing, the result remains "pending engineering determination". After that minimum gate, require all of the following:

1. `design_data.json.engineering_feasible` is `true`.
2. `status.numerical_converged` is `true`.
3. Every constraint with `blocking=true` has `passed=true`.
4. Every blocking `stage_status.status` is `completed`.
5. The CLI or orchestration exit code is `0`.
6. The solved intent revision matches the user-confirmed revision.
7. No mandatory requirement is `unsupported` or outside its model envelope.
8. Every solver-side adjustment is recorded and the complete pipeline was rerun after it.

Exit code `2` means calculation completed but the result did not converge or was engineering-infeasible. It is diagnosis input, not a deliverable candidate. A last iteration value, Class I-only result or reduced Stage 7 screening table is not a final design.

## Robustness gate

Upgrade a preliminary candidate to `robust_preliminary_feasible` only when:

- uncertainty ranges and distributions are declared and traceable;
- influential technology assumptions are included rather than held optimistically fixed;
- all blocking constraints pass the project's configured probability or conservative-margin criterion;
- the robustness run uses the same geometry, propulsion choice and requirement revision;
- failed samples and limiting margins are reported.

If the project has not declared a probability threshold or conservative margin policy, report uncertainty results without assigning the robust level.

## Full rerun invariant

After any accepted repair or optimized variable change, repeat every implemented blocking stage from Class I onward. At minimum this includes:

```text
mission and fuel fractions
Class I mass closure
constraint analysis and design point
Class II component mass closure
geometry and fuel volume
aerodynamics and propulsion
takeoff, landing, climb, cruise, ceiling and maneuver performance
stability or tail-sizing gates
uncertainty stage when enabled
```

Checking only the original failed constraint is invalid because repairs can move mass, geometry, propulsion and stability margins elsewhere.

## Model and artifact claims

The following artifacts are useful deliverables but are not validation evidence by themselves:

- `geometry.obj`;
- `geometry_mesh.json`;
- `geometry_3d.html`;
- three-view images and rendered concept images;
- `model.vspscript` when it has only been generated, not executed.

An OBJ in the workbench is a display mesh. It does not prove OpenVSP or VSPAERO execution and does not establish high-fidelity aerodynamics, inlet or propulsor integration, structural strength, fatigue, aeroelasticity, systems installation, manufacturability, control-law closure or airworthiness.

If any requirement is deferred or retained as an unsupported soft goal, the strongest user-facing conclusion is "preliminary candidate within the evaluated model scope". Always display the deferred field, retained value, coverage reason and accepted `scope_statement`; never present it as unqualified whole-aircraft feasibility.

When `range_metric_kind=evaluated_mission_distance`, label the value only as "evaluated mission distance". The prescribed segment-distance sum, including a legacy field named `actual_range_m`, is neither an independently predicted actual range nor a maximum-range capability. Use "predicted maximum range" only when `range_metric_kind=independent_capability_prediction` and the corresponding evidence identifies an independent capability model.

When a tool was actually executed, preserve command, version, input, exit code and output. When it was not executed, label the artifact as generated visualization.

## Final report checklist

Every delivered candidate report includes:

- intent ID and solved revision;
- normalized hard constraints, soft goals and design variables;
- accepted `ChangeProposal` history;
- assumptions, sources, confidence and applicability;
- numerical convergence and engineering feasibility separately;
- blocking constraint pass status and margins;
- stage completion status;
- covered, partial and unsupported requirements;
- deferred fields, retained values, coverage reasons and accepted scope statements;
- uncertainty result and limiting variables, when run;
- actual artifact paths and tool execution provenance;
- remaining high-fidelity, structure, manufacturing and certification gaps.
