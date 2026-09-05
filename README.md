# AI Agent Routing

A model-agnostic routing, escalation, and review policy for AI coding agents.

## Principle

> Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

## Structure

- `policies/MODEL_ROUTING.md` — task levels and routing rules.
- `policies/ESCALATION.md` — stop conditions and handoff protocol.
- `policies/CODE_REVIEW.md` — risk-based verification and independent review.
- `models/MODEL_REGISTRY.md` — current model-to-role mapping.
- `templates/AGENTS.minimal.md` — lightweight project template.
- `templates/AGENTS.standard.md` — general-purpose project template.
- `templates/AGENTS.high-risk.md` — domain/data-sensitive template.
- `examples/financial-project/AGENTS.md` — financial/data-integrity example.

## Routing levels

| Level | Meaning | Typical work |
|---|---|---|
| L0 | Fast / mechanical | search, rename, small edits, simple tests |
| L1 | Routine implementation | CRUD, schemas, adapters, straightforward fixes |
| L2 | Complex engineering | multi-file debugging, dependency tracing, repo-scale implementation |
| L3 | Architecture / high uncertainty | architecture, ambiguous requirements, domain semantics, difficult root cause |

## Escalation rule

For the same unresolved failure, after **two materially different unsuccessful fixes**, stop speculative editing and produce an escalation package.

Do not force every task to start at L0. High-risk or high-uncertainty tasks may route directly to L3.

## Usage

1. Copy the appropriate `templates/AGENTS.*.md` into a project as `AGENTS.md`.
2. Add project-specific rules.
3. Keep routing semantics stable.
4. Update `models/MODEL_REGISTRY.md` as models, price, or availability changes.

## Status

v0.1 — initial policy set.
