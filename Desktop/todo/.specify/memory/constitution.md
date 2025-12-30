<!--
Sync Impact Report:
Version change: 0.1.0 → 1.0.0
Modified principles:
- Spec-Driven Development as mandatory
- Agent Behavior Rules
- Phase Governance
- Technology Constraints
- Quality Principles
Added sections: None
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (MANDATORY)
No agent may write code without approved specs and tasks. All work must follow: Constitution → Specs → Plan → Tasks → Implement. This ensures traceability, quality, and alignment with business requirements.

### II. Agent Behavior Rules
No manual coding by humans, no feature invention, no deviation from approved specifications. Refinement must occur at spec level, not code level. This ensures consistency and adherence to project governance.

### III. Phase Governance
Each phase is strictly scoped by its specification. Future-phase features must never leak into earlier phases. Architecture may evolve only through updated specs and plans. This maintains clear boundaries and prevents scope creep.

### IV. Technology Constraints
Technology stack is strictly defined: Python for backend, Next.js for frontend (later phases), FastAPI, SQLModel, Neon DB, OpenAI Agents SDK, MCP, Docker, Kubernetes, Kafka, Dapr (later phases). This ensures consistency and compatibility across the project.

### V. Quality Principles
Clean architecture, stateless services where required, clear separation of concerns, cloud-native readiness. These principles ensure maintainable, scalable, and robust software systems.

### VI. Compliance and Verification
All implementations must be verifiable against their specifications. Code changes require corresponding task completion verification. This ensures accountability and quality assurance.

## Technology Standards

### Backend Requirements
Python-based backend using FastAPI framework with SQLModel for database interactions and Neon DB as the primary database. OpenAI Agents SDK and MCP protocols for agent communication.

### Frontend Requirements
Next.js-based frontend for later phases, ensuring modern, responsive user interfaces that integrate seamlessly with backend services.

### Infrastructure and Deployment
Containerized with Docker, orchestrated with Kubernetes when applicable, with event streaming via Kafka and service mesh capabilities through Dapr for advanced phases.

## Development Workflow

### Specification Adherence
All development work must strictly follow approved specifications. Any deviation requires specification update through proper channels before implementation.

### Quality Assurance
Clean architecture principles must be maintained with clear separation of concerns. Services must be stateless where required, and the system must be designed with cloud-native readiness in mind.

### Review and Approval Process
All code changes must be accompanied by evidence of task completion from the approved task list. Specifications cannot be modified at the code level.

## Governance

This constitution acts as the supreme governing document for all agents across all phases of the "Evolution of Todo" project. It supersedes all other practices and guidelines. Amendments require formal documentation, approval process, and migration planning when applicable. All agents must verify compliance with these principles during development, review, and deployment processes.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
