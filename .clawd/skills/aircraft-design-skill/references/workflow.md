# Feasibility-first Workflow

## Contents

- [1. Authoritative components](#1-authoritative-components)
- [2. Mandatory state machine](#2-mandatory-state-machine)
- [3. Intake and normalization](#3-intake-and-normalization)
- [4. Preflight and branching](#4-preflight-and-branching)
- [5. Revision and confirmation](#5-revision-and-confirmation)
- [6. Solver authorization and projection](#6-solver-authorization-and-projection)
- [7. Solver outcome feedback](#7-solver-outcome-feedback)
- [8. Repair and complete verification](#8-repair-and-complete-verification)
- [9. Delivery](#9-delivery)

## 1. Authoritative components

Use the project modules as the source of truth:

```text
src/design_intake/parser.py       natural-language intake
src/design_intake/models.py       immutable contracts and revisions
src/design_intake/coverage.py     deterministic model coverage
src/design_intake/preflight.py    diagnosis and trade proposals
src/design_intake/projection.py   solver request projection
src/design_intake/outcome.py      failed-constraint feedback revisions
src/design_intake/store.py        revisions, confirmations and submission audit
src/design_execution/             Class I/II execution and validation
external/aircraft-design-skill/   upstream engineering implementation
```

The `DesignIntent` revision is the declared requirement baseline. Solver defaults, generated reports and geometry files never override it.

## 2. Mandatory state machine

```text
user request
  -> parse and normalize
  -> preflight
     -> needs_clarification -> ask -> new or updated intent -> preflight
     -> contradictory_requirements -> propose alternatives -> user confirms -> new revision -> preflight
     -> repairable -> propose bounded changes -> apply allowed change -> new revision -> preflight
     -> unsupported -> report model gap or negotiate scope -> user confirms -> new revision -> preflight
     -> ready_for_solver -> user confirms baseline -> server can_submit -> project request -> solve
  -> solve
     -> covered constraint failure -> bounded design-variable repair -> full rerun
     -> engineering feasible -> validation and uncertainty checks
     -> nonconverged -> numerical diagnosis only -> user selects initial/design variable -> full rerun
     -> converged search exhausted -> infeasible -> evidence-backed child revision -> user confirms trade -> full rerun
  -> candidate comparison and delivery
```

Never transition directly from raw text, `needs_clarification`, `unsupported`, `contradictory_requirements` or `repairable` to solver execution.

## 3. Intake and normalization

For a natural-language request:

1. Call `looks_like_design_request` to distinguish a design job from a general explanation.
2. Call `parse_design_intent(text)` for supported Chinese or English requirement phrases.
3. Preserve unknown statements in `original_request`; do not invent values to fill parser gaps.
4. Normalize mass to `kg`, distance and altitude to `m`, duration to `s`, pressure to `Pa`, and speed ratios to `Mach`.
5. Do not convert cruise endurance into total mission range. `Mach * a * endurance` is only a cruise-segment distance diagnostic; retain it in mission metadata and ask the user to confirm total mission range because the solver also models climb and descent distance.
6. For an existing strict `AircraftDesignRequest`, use `intent_from_aircraft_request` so solver provenance becomes an explicit intent.

Read [input-schema.md](input-schema.md) before constructing or changing a contract object.

## 4. Preflight and branching

Call `preflight_design_intent(intent)` or `diagnose_design_intent(intent)`. This operation is fail-closed and does not mutate the input.

Use this branch order, which matches the implementation:

1. Explicit cross-field contradictions.
2. Blocking unsupported model coverage.
3. High-impact clarification questions.
4. Pending repair proposals.
5. `ready_for_solver`.

This ordering means an obvious logical contradiction is still reported even when one affected field also lacks a detailed model.

For every branch, show the diagnosis summary, `blocking_reasons`, relevant coverage records and current revision. Follow [dialogue-policy.md](dialogue-policy.md).

## 5. Revision and confirmation

Every accepted proposal must target the same `source_revision` and `old_value` as the current intent. Apply it through `DesignIntent.apply_change`:

- A locked target always requires `user_confirmed=true`.
- A user-provided or otherwise protected requirement requires explicit confirmation.
- An unlocked derived design variable may be changed without field-level confirmation, but its diff must be shown before the user confirms the revised baseline for solving.
- Applying a proposal increments `revision`, records `proposal_id` in `accepted_change_proposal_ids`, and resets status for another preflight.

Never edit the serialized intent in place. Reject stale proposals rather than rebasing them silently.

For an explicit conversational edit such as `change payload to 50 kg`, parse only the fields named in that message, compare them with the current revision, and show old/new values as proposals. Preserve every other field. Reject attempts to add an ambiguous new field through a partial edit; request a complete design statement or a bounded clarification instead.

## 6. Solver authorization and projection

Treat `diagnosis.ready_for_solver=true` as preflight eligibility, not authorization. After the server records explicit confirmation for that exact current revision and reports `confirmed=true` plus `can_submit=true`, call:

```python
solver_request_from_intent(intent, require_ready=True)
```

The projection must preserve the complete intent in provenance, including unsupported non-blocking soft goals. Required solver inputs include a user-confirmed positive prescribed total mission distance and non-negative payload. A cruise-segment distance diagnostic must never satisfy the solver range input.

Record each accepted submission server-side with `job_id`, `session_id`, `revision_id`, `revision_hash`, canonical request hash and `client_action_id`. The job request's client-visible provenance is not proof of ownership. Project a terminal result into a conversation workbench only when the persisted submission audit exists and its request hash matches the stored job request.

When the user explicitly accepts a covered-scope study for an out-of-envelope solver field, retain the original value under `deferred.<original_path>` as an unlocked soft goal. Materialize a separate in-envelope solver field with default provenance. Deferred fields remain in coverage, `soft_goals`, audit history and the final validation-gap report; they do not shadow or enter the active solver baseline.

The upstream no-GUI entry point is:

```bash
PYTHONPATH="${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill" \
python3 -m aircraft_design.class2_preliminary.run_sizing \
  <input.json> --project-name "<project_name>" \
  --output-dir "<output_dir>" --no-viz
```

Check Python 3.10+ and imports before direct execution. This upstream CLI is a low-level diagnostic entry point: by itself it does not enforce `DesignIntent` confirmation, model-coverage deferrals or the final scope appendix. Do not deliver its raw reports as a feasibility result. Use the project `src/design_execution` orchestration for user requirement jobs because it enforces the shared request, result, repair and delivery contracts.

## 7. Solver outcome feedback

For a terminal job whose revision and request hash match the server-owned submission audit, use this matrix:

| Result | Negotiation action |
| --- | --- |
| `engineering_infeasible` with `numerical_converged=true`, `engineering_feasible=false` and at least one structured blocking failure | Create an unconfirmed child revision. Requirement trades may be proposed only from registered mappings and finite converged evidence. |
| `nonconverged` | Create a numerical-diagnosis child revision. Ask for an initial value or registered design variable; never relax a hard requirement from the last iterate. |
| `failed`, `cancelled`, `timed_out` | Retain logs and permit retry. Do not create an engineering modification proposal. |
| `unsupported` | Report the model coverage gap. Do not infer physical infeasibility. |

For a valid converged engineering failure:

1. Read structured blocking constraints only. Preserve `id`, `required`, `actual`, `margin`, `margin_ratio`, unit and evidence.
2. Create an unconfirmed child revision. This clears the previous solve authorization.
3. Generate a requirement relaxation only when a registered constraint-to-field mapping and finite converged actual value justify the exact diff. Never apply it automatically.
4. When a failed constraint identifies a relevant design variable but no validated next value, ask for that value; do not invent one.
5. When no reliable mapping exists, report the current model-space failure and ask the user which requirement or architecture to revise.
6. Make feedback idempotent from `job_id + result_hash + parent_revision_hash`.
7. After any accepted change, run preflight, require confirmation again and execute the complete workflow.

An incomplete or internally inconsistent engineering result contract is also not trade evidence. Keep its diagnostics, fail closed and do not create a negotiation revision from it.

## 8. Repair and complete verification

Solver-side repair may adjust only registered, unlocked design variables within declared bounds. User mission requirements remain unchanged.

Technology assumptions are not free repair variables. Change `cd0`, `oswald_e`, TSFC, BSFC, propulsive efficiency or material properties only after selecting a traceable technology or component source with a valid applicability envelope.

After every repair:

1. Start again at Class I mission and mass closure.
2. Recompute constraint analysis, Class II mass, geometry, fuel volume, propulsion, performance and stability stages.
3. Re-evaluate every blocking constraint, not only the constraint that triggered repair.
4. Retain trigger, old value, new value, bounds, reason and all rerun results in `design_adjustments`.
5. Stop after the declared attempt or search limit. Do not relax hard requirements automatically.

## 9. Delivery

Use [validation-levels.md](validation-levels.md) to assign the result state. Deliver at least:

- normalized requirement baseline and revision;
- accepted changes and unresolved tradeoffs;
- assumptions with source and confidence;
- model coverage and validation gaps;
- candidate metrics and blocking constraint margins;
- numerical convergence and engineering feasibility separately;
- reproducibility metadata and actual artifact paths.

At the compact Web/job boundary, a passing engineering gate requires all three values exactly: `engineering.numerical_converged === true`, `engineering.engineering_feasible === true`, and `engineering.blocking_failed_count === 0`. If any value is absent, keep the result at "pending engineering determination".

If any `deferred.*`, scope deferral or unsupported soft goal remains, use only the scoped wording "preliminary candidate within the evaluated model scope" and show a specialty-validation-gap table with the retained value, reason and scope statement. Never use an unqualified whole-aircraft feasibility title.

Report `range_metric_kind=evaluated_mission_distance` only as "evaluated mission distance", even when the compatibility field is named `actual_range_m`. Do not call it actual range, achieved range or maximum range; it is the distance prescribed to and accounted for by the segment mission. A maximum-range claim requires `range_metric_kind=independent_capability_prediction` and independent capability evidence.

When several candidates pass, rank them only after hard constraints pass. Prefer maximum minimum margin first, then declared soft-goal score and secondary objectives such as mass or cost.
