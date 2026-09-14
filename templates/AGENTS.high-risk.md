# High-Risk Agent Rules

Follow `templates/AGENTS.standard.md` plus these stricter rules.

Treat architecture, public interfaces/schemas, provenance, identity, timestamps/order, historical mutation, financial/domain interpretation, security boundaries, and safety-critical behavior as L3 decision work unless an authoritative source has already settled the decision.

Missing evidence fails closed. Never infer values or semantics merely to continue. Preserve raw inputs, provenance, immutable history, information cutoffs, and deterministic calculations where applicable.

High-risk initial IMPLEMENT and every Blocker/Major finding correction require fresh independent REVIEW. The implementing session sets `FIXED-PENDING-REVIEW`; only the fresh reviewing session may set `FIXED`.

Session authorization remains mandatory. A model's name, tier, provider, or self-assessment never grants permission above Maximum authorized level.
