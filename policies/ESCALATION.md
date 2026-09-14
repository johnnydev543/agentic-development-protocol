# Escalation Policy

Escalation means stopping unauthorized or low-confidence work and returning a concise evidence package.

If the required task level exceeds `Maximum authorized level`, stop immediately before planning, architectural decomposition, design, or edits. Correctly detecting a higher level does not authorize the agent to perform it.

## L0 / L1

After 2 materially different unsuccessful fixes for the same failure:

- STOP.
- Do not make a third speculative modification.
- Recommend L2 for an engineering/debugging problem.
- Recommend L3 directly for architecture, domain semantics, provenance, timing, or other high-risk decisions.

## L2

After 2 materially different unsuccessful fixes:

- STOP.
- Recommend L3 when deeper root-cause analysis, architecture, or domain judgment is required.
- Do not broaden refactoring merely to make tests pass.

## L3

If already at L3, do not recommend L3 again merely because the task is difficult.

Stop and request clarification or independent review when authoritative semantics are missing, required source data is unavailable, requirements conflict, or the next step would require inventing domain rules or values.

## Immediate Stop Conditions

Stop at any level when:

1. The same failure remains unresolved after 2 materially different fixes.
2. A fix causes the original failure to reappear.
3. Fixing one component repeatedly breaks another.
4. Root cause cannot be identified from code, logs, tests, or documented behavior.
5. The next step requires guessing business/domain semantics, mappings, timestamps, or numeric values.
6. The solution requires an architectural redesign not authorized by the specification.
7. Implementation conflicts with written project rules.
8. The agent is repeating a prior approach without new evidence.
9. Tests pass but intended behavior is still reasonably doubtful.

## Required Escalation Package

```text
### ESCALATION REQUIRED

Current routing level:
<L0 / L1 / L2 / L3 / unknown>

Maximum authorized level:
<L0 / L1 / L2 / L3>

Recommended next level:
<L1 / L2 / L3 / clarification / independent review>

Reason:
<why escalation is required>

Current task:
<original requested change>

Observed failure:
<exact behavior, error, or test>

What has been tried:
<materially different attempts and outcomes>

Suspected root cause:
<evidence-supported hypotheses; mark uncertainty>

Relevant files:
<files involved>

Relevant tests:
<failing or related tests>

Important constraints:
<applicable project rules/specification constraints>

Next question:
<precise diagnosis, clarification, or decision needed>
```

The package should let a newly authorized session continue without reconstructing failed attempts from scratch.
