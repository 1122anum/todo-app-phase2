---
id: 1
title: Create Global Constitution
stage: constitution
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 003-book-impact-widget
user: Tech Trends
command: /sp.constitution
labels: [constitution, governance, spec-driven-development]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

Create a single global constitution for the entire "Evolution of Todo" project
covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory
   - No agent may write code without approved specs and tasks
   - All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules
   - No manual coding by humans
   - No feature invention
   - No deviation from approved specifications
   - Refinement must occur at spec level, not code level

3. Phase Governance
   - Each phase is strictly scoped by its specification
   - Future-phase features must never leak into earlier phases
   - Architecture may evolve only through updated specs and plans

4. Technology Constraints
   - Python for backend
   - Next.js for frontend (later phases)
   - FastAPI, SQLModel, Neon DB
   - OpenAI Agents SDK, MCP
   - Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles
   - Clean architecture
   - Stateless services where required
   - Clear separation of concerns
   - Cloud-native readiness

This constitution must remain stable across all phases
and act as the supreme governing document for all agents.

## Response snapshot

A new constitution has been created for the "Evolution of Todo" project. The constitution establishes five core principles:

1. Spec-Driven Development (MANDATORY) - requiring all work to follow Constitution → Specs → Plan → Tasks → Implement
2. Agent Behavior Rules - prohibiting manual coding by humans and deviations from approved specifications
3. Phase Governance - maintaining strict phase boundaries and preventing feature leakage
4. Technology Constraints - defining the technology stack for the project
5. Quality Principles - establishing clean architecture and cloud-native readiness requirements

The constitution also includes sections on Technology Standards, Development Workflow, and Governance. It acts as the supreme governing document for all agents across all phases of the project.

## Outcome

- ✅ Impact: Created comprehensive project constitution that defines governance for all phases
- 🧪 Tests: N/A
- 📁 Files: Updated .specify/memory/constitution.md with new constitution content
- 🔁 Next prompts: Continue with spec, plan, and task creation following the new constitution
- 🧠 Reflection: The constitution provides a solid foundation for consistent development across all project phases

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating specifications following the new constitution guidelines