# Architecture Pass Prompt Template

Use this when the specification is already settled and a strong model should establish the main code architecture without completing the entire product.

```text
You are responsible for the architecture implementation phase of this project.

The specification is already decided. Treat the authoritative specification, AGENTS.md, README, and existing code as sources of truth. Do not redesign product requirements or expand scope.

Your goal is NOT to complete the entire project. Your goal is to establish a stable implementation architecture that lower-cost coding models can safely continue.

Complete:
1. Project/module/package boundaries.
2. Core domain models, interfaces, protocols, schemas, and types.
3. Dependency direction and ownership boundaries.
4. High-risk, architectural, or cross-module core logic.
5. Application entry point / bootstrap / dependency injection.
6. Shared config, logging, and error-handling foundations.
7. Required repository/service/provider abstractions.
8. Main API/CLI/worker/pipeline skeletons.
9. At least one representative reference implementation for important extension patterns.
10. Minimal smoke/architecture tests proving the system composes, imports/builds, and starts.

Unless architecture requires it, DO NOT:
- finish all CRUD;
- finish every endpoint/provider/adapter;
- fill all repetitive boilerplate;
- implement every edge case;
- write exhaustive coverage;
- polish UI;
- optimize prematurely;
- expand the specification.

Rule:
Architecture decisions should be made now.
Repetitive implementation should be delegated later.

Create or update docs/implementation-handoff.md with:
- Architecture completed
- Architecture invariants
- Remaining implementation tasks
- High-risk remaining work

Each remaining task should include:
- task ID and status;
- relevant files/modules;
- goal;
- implementation notes;
- explicit "do not change" boundaries;
- acceptance criteria;
- required tests.

Prefer tasks that can be implemented independently and normally affect only 1-3 modules.

TODOs must reference a concrete task ID and expected behavior. Do not leave vague TODOs.

Before stopping:
1. Run relevant tests.
2. Run configured lint/type checks.
3. Confirm build/import/startup succeeds as appropriate.
4. Confirm remaining tasks can be completed without reinterpreting architecture.

If a remaining item still requires architecture or domain judgment, list it under High-risk remaining work instead of delegating it as routine implementation.

Then STOP. Do not continue implementing the remaining tasks yourself.
```
