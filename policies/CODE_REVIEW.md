# Code Review Policy

Verification and review are risk-based. Do not spend expensive independent review on every trivial change.

## Standard Verification

For ordinary changes, complete the relevant subset of:

1. Unit tests.
2. Integration tests, if available.
3. Lint checks, if configured.
4. Type checks, if configured.

## Independent Review

Independent review is required or strongly preferred for high-risk changes, including:

- Financial or safety-critical calculations.
- Domain-semantic extraction or normalization.
- Consensus/revision logic.
- Historical data mutation rules.
- Database schema changes affecting important data.
- Identity/mapping logic.
- Timestamp/information-cutoff logic.
- Source provenance logic.
- Backtesting logic.
- Cross-module architecture changes.
- Large refactors affecting domain behavior.

Prefer a fresh-context reviewer different from the implementation model when practical.

## Reviewer Input

The reviewer should receive:

- Original task.
- Authoritative specification.
- Relevant project rules.
- Git diff.
- Test/lint/type-check output.

## Finding Severity

Classify findings as:

- Blocker
- Major
- Minor
- Suggestion

The reviewer must not silently rewrite domain semantics. Any finding that changes authoritative business/domain meaning must be supported by a source/specification or escalated for clarification.

## Cross-Model Review

Cross-model review is useful for independent error detection, not automatic deference to a supposedly stronger model. Prefer diversity of model perspective when the change is high-risk or when the implementer may have anchored on a flawed assumption.
