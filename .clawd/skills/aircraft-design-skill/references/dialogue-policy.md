# Feasibility Dialogue Policy

## Contents

- [Objective](#objective)
- [First response to a design request](#first-response-to-a-design-request)
- [Question policy](#question-policy)
- [Status-specific behavior](#status-specific-behavior)
- [Change confirmation protocol](#change-confirmation-protocol)
- [Technology assumptions](#technology-assumptions)
- [Candidate presentation](#candidate-presentation)

## Objective

Every turn must move the current `DesignIntent` toward a confirmed, testable baseline without hiding conflicts or changing protected requirements. A useful answer is not always a feasible aircraft; it may be a bounded clarification, a model-gap statement or a quantified trade proposal.

## First response to a design request

Show a compact requirement baseline before asking for changes:

1. Current `intent_id` and `revision`.
2. Locked hard constraints.
3. Soft goals and unlocked design variables.
4. Default, derived and reference assumptions with confidence.
5. Model coverage and the highest-impact risks.
6. Current diagnosis status and next decision.

Do not show a long generic explanation of the skill. Talk about the user's aircraft and the decision that blocks progress.

## Question policy

Ask only when a missing or ambiguous item materially affects architecture, mass closure, model selection or solver authorization. Present at most 3 high-impact questions in one turn.

Each `ClarificationQuestion` must include:

- one field path;
- the engineering reason;
- 2 or 3 bounded options when choices are known;
- one recommended option with its tradeoff;
- what happens if the user does not answer.

Do not ask for parameters that the deterministic solver can safely derive or search. Do not invent a propulsion type for a high-speed request when that choice materially changes the design.

Cruise endurance does not determine total mission range without climb, descent and mission-profile assumptions. Show `Mach * a * endurance` only as a cruise-segment distance diagnostic and ask the user to confirm total mission range. Until an independent fuel-limited endurance capability model is registered, retain minimum cruise endurance as a validation gap rather than treating a prescribed segment time as achieved capability.

## Status-specific behavior

### `needs_clarification`

Ask the returned blocking questions. Keep missing values absent. After the answer, build or update the intent and run preflight again.

### `unsupported`

State all three facts clearly:

1. Which mandatory field has no applicable model.
2. Why this is a model coverage gap rather than evidence of physical infeasibility.
3. Which covered subproblem can still be evaluated, if any.

Offer bounded next paths, such as adding a specialty model, removing or softening the unsupported requirement with user approval, or accepting a clearly labeled covered-scope study. Never mark the full aircraft feasible from a partial study.

### `contradictory_requirements`

Show the minimal conflicting field set and at least 2 alternatives when available. For each alternative show old value, proposed value, benefit and engineering cost. Do not select an alternative for the user.

### `repairable`

Separate two classes of proposal:

- Unlocked design-variable change: may be applied within bounds, but show the diff and re-run preflight before solving.
- Locked or user-provided requirement change: require explicit user confirmation before applying it.

Use decision-oriented labels such as "preserve MTOW", "preserve payload" and "balanced trade" only when the underlying numeric proposals come from deterministic checks or optimization.

### `ready_for_solver`

Summarize the exact baseline and request explicit confirmation. The diagnosis alone does not authorize calculation. Submit only when the server-owned current revision reports `confirmed=true` and `can_submit=true`; even then, this is not a feasibility result.

### `infeasible`

Use this state only after applicable covered models execute and a declared bounded search is exhausted. Report the failed constraints, closest margins, search bounds and at least 2 quantified requirement trade options when possible. Do not use it for missing models or execution errors.

## Change confirmation protocol

A user confirmation must identify a proposal or unambiguously name the field and new value. Then:

1. Verify `source_revision` and `old_value` against the current intent.
2. Call `apply_change` with `user_confirmed=true` when required.
3. Show the revision diff and accepted proposal ID.
4. Re-run the entire preflight.
5. Do not start the solver until the new revision is `ready_for_solver` and the baseline is confirmed.

Do not interpret "continue" as permission to alter an unrelated locked constraint. If multiple trade paths remain, ask the user to choose one.

Do not interpret "continue", "calculate directly" or similar text as solver authorization. Re-display the current revision interaction until its explicit confirmation and submit actions are complete. A natural-language edit with an unambiguous field and value becomes a diff against the current revision, not a replacement intent.

After a failed deterministic run, show the failed constraint's required value, actual value and margin before any proposed change. A proposal based on the last modeled capability is a new hypothesis that requires a complete rerun; it is not proof that the next revision will pass.

For `nonconverged`, do not treat the last iterate as modeled capability and do not derive a hard-requirement relaxation from it. Ask for an initial value or bounded design-variable decision, or offer a numerical retry. Only a numerically converged `engineering_infeasible` result may support an evidence-backed requirement trade.

## Technology assumptions

Never propose a more optimistic technology value as a free mathematical repair. A technology change must name its source or component, applicability envelope, expected maturity and affected constraints. Examples include engine TSFC, propeller efficiency, `cd0`, `oswald_e`, CLmax and material allowables.

If no evidence exists, retain the current assumption, identify sensitivity, and offer a requirement or architecture trade instead.

## Candidate presentation

After validation, compare only candidates that pass the relevant hard gates. Present:

| Item | Required content |
| --- | --- |
| Requirement fit | Pass or margin for every hard constraint. |
| Revisions | Every user-confirmed and automatic unlocked-variable change. |
| Technology basis | Source and applicability of influential assumptions. |
| Model fidelity | Covered, partial and unsupported items. |
| Robustness | Nominal margin and uncertainty result when available. |
| Artifacts | Report, data, geometry and images with actual paths. |

Do not hide a failed candidate by showing only attractive geometry or headline metrics.
