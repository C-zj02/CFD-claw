# Design Intake Contract

This reference mirrors `src/design_intake/models.py`. Code is authoritative if the contract changes.

## Contents

- [RequirementField](#requirementfield)
- [DesignIntent](#designintent)
- [Intent and diagnosis states](#intent-and-diagnosis-states)
- [ClarificationQuestion](#clarificationquestion)
- [ChangeProposal](#changeproposal)
- [ModelCoverageRecord](#modelcoveragerecord)
- [FeasibilityDiagnosis](#feasibilitydiagnosis)

## RequirementField

Each normalized value is represented independently:

```json
{
  "path": "requirements.cruise_mach",
  "value": 0.6,
  "unit": "Mach",
  "role": "hard_constraint",
  "locked": true,
  "source": "user",
  "tolerance": null,
  "confidence": 1.0,
  "applicable_model": null,
  "source_reference": null
}
```

Allowed `role` values:

| Value | Meaning | Default modification rule |
| --- | --- | --- |
| `hard_constraint` | Mandatory performance or geometry bound | Lock user-declared values. Never change silently. |
| `soft_goal` | Preference or ranking objective | May be traded, but preserve it in provenance and explain deviations. |
| `design_variable` | Quantity the solver may search | Keep unlocked unless the user explicitly fixes it. Enforce declared bounds. |
| `technology_assumption` | Aero, propulsion, material or systems capability assumption | Change only with a traceable source and applicable envelope. |

Allowed `source` values are `user`, `derived`, `default` and `reference`. A `reference` value requires `source_reference`. A derived value must preserve its derivation in `applicable_model` or provenance. `confidence` is between 0 and 1. `tolerance` is non-negative and uses the field unit.

Classification rules:

- Wording such as "must", "shall", "at least", "not less than" and "not greater than" maps to a locked hard constraint.
- Wording such as "prefer", "reference", "approximately" and "if possible" maps to a soft goal unless the user says it is mandatory.
- User-selected geometry or sizing values are hard constraints when fixed and design variables when explicitly left for optimization.
- `cd0`, `oswald_e`, TSFC, BSFC, propeller efficiency, CLmax and material allowables are technology assumptions, not convenient repair knobs.
- Never reinterpret a failed hard constraint as a soft goal.

## DesignIntent

`DesignIntent` is the immutable source of truth:

```text
intent_id
requirements[]
revision
status
original_request
mission
aircraft_class
configuration
propulsion
launch
recovery
metadata
accepted_change_proposal_ids[]
```

Field paths use dotted ASCII identifiers. Common paths include:

```text
requirements.range_m
requirements.payload_kg
requirements.cruise_mach
requirements.cruise_altitude_m
requirements.service_ceiling_m
requirements.propulsion_type
weights.max_mtow_kg
performance.min_cruise_endurance_s
performance.max_flight_mach
geometry.max_aspect_ratio
launch.mode
launch.field_altitude_m
launch.booster_end_mach
launch.booster_end_relative_altitude_m
recovery.mode
recovery.parachute_open_mach
recovery.parachute_open_relative_altitude_m
propulsion.engine_count
configuration.reference
configuration.stealth_requirement
initial_guess.mtow_kg
initial_guess.wing_loading_pa
initial_guess.thrust_to_weight
initial_guess.aspect_ratio
```

Do not insert defaults during natural-language parsing. Missing high-impact values belong in clarification. Solver defaults are introduced only during projection and remain labeled `default` or `derived`.

`performance.min_cruise_endurance_s` and `requirements.range_m` have different semantics. The former is cruise-segment time; the latter is the user-prescribed total mission distance used to synthesize and evaluate the modeled climb, cruise and descent segments. It is not an independently predicted maximum-range capability. Never create it with `Mach * a * endurance`. Store that product only as `mission.minimum_cruise_segment_distance_m` diagnostic metadata, and require the user to confirm the prescribed total mission distance.

An explicitly deferred out-of-envelope solver input uses `deferred.<original_path>`. This is a retained soft goal and model gap, not an active solver input. The active replacement field keeps its normal path and explicit `default` or `derived` source.

## Intent and diagnosis states

Allowed `status` values:

| State | Meaning |
| --- | --- |
| `needs_clarification` | Required or high-impact information is missing. |
| `unsupported` | A mandatory field has no registered applicable model. This is not physical infeasibility. |
| `contradictory_requirements` | Explicit fields conflict logically. |
| `infeasible` | Covered models and the declared search space show no passing candidate. |
| `repairable` | Explicit bounded changes are available but not yet incorporated into the baseline. |
| `ready_for_solver` | Preflight passed and the revision is eligible for explicit confirmation. This diagnosis does not authorize a solver submission. |
| `conceptually_feasible` | Concept-level gates passed at the stated model fidelity. |
| `preliminary_feasible` | Full implemented Class I/II blocking gates passed. |
| `robust_preliminary_feasible` | Preliminary gates and declared uncertainty or margin checks passed. |

## ClarificationQuestion

```text
question_id
field_path
question
reason
options[]
recommended_option
consequence_if_unanswered
blocking
```

Questions are bounded decisions, not open-ended interviews. A recommendation must be one of the supplied options.

## ChangeProposal

```text
proposal_id
field_path
old_value
proposed_value
reason
affected_constraints[]
expected_benefit
engineering_cost
target_locked
requires_user_confirmation
source_revision
```

A proposal is evidence, not an applied change. `old_value` and `source_revision` are stale-write guards. Any `target_locked=true` proposal must have `requires_user_confirmation=true`.

Applying a valid proposal creates a new revision and records its ID. It never overwrites history.

## ModelCoverageRecord

```text
field_path
status
model_id
reason
applicable_envelope
blocking
```

Allowed coverage status values are `covered`, `partial` and `unsupported`. `partial` and `unsupported` require a reason. An unknown field fails closed as `unsupported`. Unsupported hard constraints and non-soft fields block solving; an unsupported soft styling preference may be non-blocking but must stay visible.

## FeasibilityDiagnosis

```text
status
summary
coverage[]
clarification_questions[]
change_proposals[]
blocking_reasons[]
conflicting_fields[]
assumptions[]
ready_for_solver
```

`ready_for_solver=true` is invalid when a blocking reason, blocking question or blocking coverage record remains. A diagnosis never mutates its input intent.
