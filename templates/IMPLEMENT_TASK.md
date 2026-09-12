# Delegated Implementation Prompt Template

Use this with a lower-cost coding model after the architecture pass has produced explicit handoff tasks.

```text
Execute <TASK-ID> from docs/implementation-handoff.md.

Before editing, read:
- AGENTS.md
- docs/implementation-handoff.md
- the selected task
- the files/tests directly referenced by that task

Scope is limited to <TASK-ID>.

Requirements:
1. Follow the existing architecture, interfaces, schemas, dependency direction, and reference implementation patterns.
2. Implement only the selected task.
3. Add or update the tests required by the task.
4. Run the relevant tests plus configured lint/type checks for the affected scope.
5. Do not modify unrelated files or refactor unrelated code.
6. Do not redesign module boundaries, public interfaces, schemas, or dependency direction unless the task explicitly authorizes it.
7. If completion requires an architectural or domain-semantic change, STOP and report the blocker instead of silently redesigning the system.

When complete, update docs/implementation-handoff.md:
- set <TASK-ID> to DONE only if verification passes;
- record changed files;
- record verification commands/results;
- add any concrete follow-up task discovered during implementation.

Do not automatically start another task.
```
