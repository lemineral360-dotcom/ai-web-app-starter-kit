# Task Board — initial project state

All project gates PENDING. Owner assigns tasks; use handoff/TASK-LOCK.md when coordinating multiple agents.

| ID | Task | Dependency | Status |
|---|---|---|---|
| P-001 | Discovery, intake, PRD | none | TODO |
| P-002 | Owner Planning Gate | P-001 | TODO |
| D-001 | UX, design system, prototype | P-002 | TODO |
| D-002 | Owner Design Gate | D-001 | TODO |
| A-001 | Architecture, data, API, security | D-002 | TODO |
| A-002 | Owner Architecture Gate | A-001 | TODO |
| I-001 | Implement approved feature specs | A-002 | TODO |
| Q-001 | QA and independent review | I-001 | TODO |
| R-001 | Owner Release Gate | Q-001 | TODO |

Add real feature tasks, acceptance criteria, owners, branches and evidence when planning. Never mark DONE without evidence.
