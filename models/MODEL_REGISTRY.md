# Model Registry

Last reviewed: 2026-09-05

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

### Ollama Cloud
Prefer for access to GLM, Kimi, DeepSeek, and other cloud models, especially when cost-efficient implementation or model specialization is useful.

### OpenRouter
Prefer as a broad model exchange layer for:
- independent second opinions,
- A/B model evaluation,
- specialist models,
- model/provider fallback.

## Maintenance Rule

Do not change `policies/MODEL_ROUTING.md` merely because a new model becomes available. Update this registry first. Change routing policy only when the underlying workflow principle changes.

Model placement here is operational guidance, not a permanent benchmark ranking. Re-evaluate it against real project outcomes.
