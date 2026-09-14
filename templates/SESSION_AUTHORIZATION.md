# Session Authorization Header

Copy this header into every working session.

```text
SESSION AUTHORIZATION

Role: <PLAN / PLAN-REVIEW / IMPLEMENT / REVIEW / REVIEW-AND-FIX / DECISION>
Maximum authorized level: <L0 / L1 / L2 / L3>
Task: <optional natural-language scope>

You may classify the required work at any L0-L3 level. Classification does not grant execution authority.

Keep this role for the entire session. Infer the required task level and effective scope from the request, current changes, branch/checkpoint state, and review ledger. State them before acting. Ask for scope only when multiple unrelated targets or an unsafe ambiguity prevents reliable inference.

If any required work exceeds Maximum authorized level:
- do not plan or architecturally decompose it;
- do not design, edit files, or implement;
- output only ESCALATION_REQUIRED and the required escalation package;
- stop immediately.
```
