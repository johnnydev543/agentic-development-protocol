# Delegated Implementation Prompt Template

Use this with a lower-cost coding model after the architecture pass has produced explicit handoff tasks.

```text
Execute <TASK-ID> from docs/implementation-handoff.md.

Before editing, read:
- AGENTS.md
- docs/implementation-handoff.md
- the selected task
- the files/tests directly referenced by that task

The project rules and selected task are authoritative. Do not load unrelated lifecycle templates, historical reviews, or model-selection documents.

Scope is limited to <TASK-ID>.

Follow the recorded architecture and implement only the selected task. Add its tests and run the relevant checks. Do not refactor unrelated code. If completion requires changing an invariant, interface/schema, dependency direction, or domain meaning, STOP and report the blocker.

When complete, update docs/implementation-handoff.md:
- set <TASK-ID> to DONE only if verification passes;
- record changed files;
- record verification commands/results;
- add any concrete follow-up task discovered during implementation.

Do not automatically start another task.
```
