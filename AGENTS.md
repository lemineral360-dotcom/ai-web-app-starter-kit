# AGENTS — shared rules
## Start
Read START_HERE.md, docs/PRD.md, docs/TASKS.md, docs/HANDOFF.md and docs/DECISIONS.md. Verify repo, branch, task ownership and actual gate status. Read only relevant role, specs and phase documents via handoff/CONTEXT.md. Beginner mode is default; ask one important question at a time, explain costs and risks, fill documents for the owner.
## Gates
Planning → Design → Architecture → Development → QA → Release → authorized deployment. All new project gates PENDING. No application implementation anywhere before Planning, Design and Architecture are APPROVED by owner. Design artifacts and documentation allowed before implementation. Release approval and explicit production authorization required. Record exact revision, date, owner and evidence. Never infer approval.
## Canonical sources
PRD: scope; DECISIONS: decisions; TASKS: work; HANDOFF: current state; ARCHITECTURE: technical decisions; design/DESIGN.md: visual direction; design/DESIGN_APPROVAL.md: approved artifact revision. Resolve conflicts with owner; approved changes require docs/CHANGE_REQUEST.md.
## Execute
One scoped task with acceptance criteria. Follow guides/DESIGN_WORKFLOW.md or guides/ENGINEERING_WORKFLOW.md and relevant engineering standards. Verify tool access; no invented artifacts. Use least privilege, synthetic data, no secrets in repo. Explicit permission for destructive changes.
## Quality
Apply quality/ANTI_AI_SLOP.md and quality/REVIEW.md. Run relevant tests; distinguish PASS, FAIL, NOT RUN, BLOCKED. Critical findings block release regardless of score. Independent review when available; do not mislabel self-review.
## Handoff
Follow handoff/PROTOCOL.md; update TASKS and HANDOFF with actual changes, tests, blockers, next task and revision. Parallel work requires separate ownership/branches and integrator. Optional dispatcher is not an approval authority or sandbox. Report phase, verified result, decision and next step using templates/PROJECT_STATUS.md.
