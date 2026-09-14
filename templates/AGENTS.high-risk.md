# High-Risk Agent Rules

Follow `templates/AGENTS.standard.md` plus these stricter rules.

Treat architecture, public interfaces/schemas, provenance, identity, timestamps/order, historical mutation, financial/domain interpretation, security boundaries, and safety-critical behavior as L3 decision work unless an authoritative source has already settled the decision.

Missing evidence fails closed. Never infer values or semantics merely to continue. Preserve raw inputs, provenance, immutable history, information cutoffs, and deterministic calculations where applicable.

High-risk IMPLEMENT and every Blocker/Major FIX require fresh independent REVIEW or RE-REVIEW. The fixer sets `FIXED-PENDING-REVIEW`; only the independent re-reviewer may set `FIXED`.

Session authorization remains mandatory. A model's name, tier, provider, or self-assessment never grants permission above Maximum authorized level.
