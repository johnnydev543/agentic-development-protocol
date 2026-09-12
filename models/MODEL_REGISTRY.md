# Model Registry

Last reviewed: 2026-09-12

This file is intentionally separate from routing policy because model availability, pricing, and capability change faster than routing principles.

## Current Mapping

### L0 — Fast / Mechanical
- GPT-5.6 Luna
- DeepSeek V4 Flash

### L1 — Routine Implementation
- GLM-5.3 Flash
- GPT-5.6 Terra

### L2 — Complex Engineering
- GLM-5.3
- DeepSeek V4 Pro
- GPT-5.6 Terra when appropriate

### L3 — Architecture / High Uncertainty
- GPT-5.6 Sol

## Recommended Role Mapping

This is a practical default for the staged workflow, not a hard requirement.

### ARCHITECT
Prefer:
- GPT-5.6 Sol
- GLM-5.3 when the architecture is relatively conventional and domain risk is moderate
- another independently validated strong engineering model when appropriate

Use the architect for architecture decisions, interface/schema design, dependency direction, representative reference implementations, and high-risk cross-module logic. Stop when the remaining work is deterministic enough to delegate.

### IMPLEMENT
Prefer:
- GLM-5.3 Flash for clear implementation tasks
- GPT-5.6 Terra for routine-to-complex implementation inside Codex
- GPT-5.6 Luna or DeepSeek V4 Flash for mechanical/local tasks
- GLM-5.3 / DeepSeek V4 Pro when the task is implementation-heavy but still requires substantial repository reasoning

### REVIEW
Prefer a fresh context and, when practical, a different model family from the implementer.

For important changes:
- GPT-5.6 Sol
- GLM-5.3
- DeepSeek V4 Pro
- other strong independent engineering models available through OpenRouter after task-specific evaluation

The review model should diagnose and produce structured findings; it does not automatically need to perform the fixes.

### REVIEW FIX
Prefer:
- GLM-5.3 Flash / GPT-5.6 Terra for explicit localized fixes
- GPT-5.6 Luna / DeepSeek V4 Flash for mechanical fixes

Escalate back to GPT-5.6 Sol or another L3-capable model when the finding requires architecture/schema/interface changes, unsupported domain judgment, or uncertain cross-module root-cause reasoning.

### VERIFY
Prefer the cheapest model/harness that can reliably execute and interpret the required tests, lint, type checks, build, and smoke checks. Verification should not consume strong-model capacity unless failures themselves become uncertain or architectural.

## Specialists

### Frontend / UI
- Kimi K3

### Independent Engineering Alternatives
- GLM-5.3
- DeepSeek V4 Pro
- Other strong models available through OpenRouter after task-specific evaluation

## Provider Roles

### Codex
Prefer when repository-aware agent execution, editing, tests, and an integrated coding harness are valuable.

Available primary family:
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna

A useful pattern is Sol for architecture/review, then Terra/Luna for scoped implementation and fixes when the architecture is already explicit.

### Ollama Cloud
Prefer for access to GLM, Kimi, DeepSeek, and other cloud models, especially when cost-efficient implementation or model specialization is useful.

GLM-5.3 Flash is a good default candidate for repetitive, pattern-following implementation after a strong model has established the architecture.

### OpenRouter
Prefer as a broad model exchange layer for:
- independent second opinions,
- A/B model evaluation,
- specialist models,
- model/provider fallback.

Provider-side prompt caching can materially change effective cost for long, repeated contexts; evaluate real workload cost instead of comparing nominal token prices alone.

## Session and Cache Considerations

Model/provider prompt caches are generally model/provider-specific. Do not assume that switching models preserves the same cache benefit.

For coding workflows, stable project instructions and repeated repository context may produce more cache reuse than frequently rebuilding unrelated sessions, but correctness and clean review context take precedence over cache optimization.

Use repository handoff files and Git diffs to move state across sessions rather than keeping one session alive solely for context continuity.

## Maintenance Rule

Do not change `policies/MODEL_ROUTING.md` merely because a new model becomes available. Update this registry first. Change routing policy only when the underlying workflow principle changes.

Model placement here is operational guidance, not a permanent benchmark ranking. Re-evaluate it against real project outcomes, latency, provider reliability, cache behavior, and total cost.
