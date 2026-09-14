# Session Authorization Header

Copy this header into every working session.

```text
SESSION AUTHORIZATION

Role: <PLAN / PLAN-REVIEW / IMPLEMENT / REVIEW / REVIEW-AND-FIX / FIX / RE-REVIEW / DECISION>
Assigned execution level: <L0 / L1 / L2 / L3>
Maximum authorized level: <L0 / L1 / L2 / L3>
Task or review scope: <explicit task, finding IDs, files, or components>

You may classify the required work at any L0-L3 level. Classification does not grant execution authority.

If any required work exceeds Maximum authorized level:
- do not plan or architecturally decompose it;
- do not design, edit files, or implement;
- output only ESCALATION_REQUIRED and the required escalation package;
- stop immediately.
```
