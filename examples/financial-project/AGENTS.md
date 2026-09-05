# AGENTS.md — Financial Project Example

## Financial Data

- Never invent financial values.
- Every extracted or normalized financial value must remain traceable to its source.
- Missing values remain missing; do not silently substitute zero or model estimates.
- Preserve original source content and source identifiers.

## Historical Integrity

- Do not overwrite historical forecasts or revisions when history is part of the dataset.
- Re-extraction by an LLM is not itself a market-expectation revision.
- Preserve report/announcement timestamps required to reconstruct the information set available at a historical point in time.

## Backtesting

- Prevent look-ahead bias.
- Use only information available at the simulated decision timestamp.
- Treat information-cutoff logic as high risk.

## Routing

- L0: repository search, localized edits, simple tests.
- L1: routine implementation from explicit financial/data specifications.
- L2: complex multi-file engineering where financial semantics are already defined.
- L3: financial interpretation, forecast/expectation semantics, revision ordering, provenance, information cutoff, look-ahead-bias decisions, architecture.

Do not make a lower-tier model guess financial semantics merely to keep implementation moving.

## Escalation

After 2 materially different unsuccessful fixes for the same failure, STOP and escalate.

Stop immediately if the next step requires inventing or guessing:

- financial values,
- forecast periods,
- company/ticker identity,
- market classification,
- report dates or announcement timestamps,
- revision ordering,
- consensus rules,
- information cutoff,
- source provenance.

Provide the standard escalation package from `policies/ESCALATION.md`.

## Review

Independent review is strongly preferred for financial calculations, extraction semantics, consensus/revision logic, normalization, ticker/company mapping, market classification, timestamp/information-cutoff logic, provenance, backtesting, and database changes affecting historical financial data.

The reviewer must not silently rewrite financial meaning. Any semantic change must be supported by the authoritative specification/source or escalated for clarification.
