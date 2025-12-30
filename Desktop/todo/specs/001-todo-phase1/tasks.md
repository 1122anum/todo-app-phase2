---
description: "Task list for Phase I Todo Console Application implementation"
---

# Tasks: Phase I - In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-todo-phase1/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with src/ and tests/ directories
- [x] T002 Create src/todo_app.py file as main application file
- [x] T003 [P] Create tests/ directory structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Define Task data model class in src/todo_app.py
- [x] T005 [P] Define TaskList collection class in src/todo_app.py
- [x] T006 [P] Implement CLI menu structure and application loop in src/todo_app.py
- [x] T007 Create input validation and error handling utilities in src/todo_app.py
- [x] T008 [P] Implement application startup and exit flow in src/todo_app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement ability to add new tasks to the todo list with unique IDs

**Independent Test**: Can be fully tested by adding various task descriptions and confirming they appear in the task list with unique IDs.

### Implementation for User Story 1

- [x] T009 [P] [US1] Implement Task constructor with ID, description, and completion status in src/todo_app.py
- [x] T010 [US1] Implement TaskList.add_task() method that creates tasks with unique sequential IDs in src/todo_app.py
- [x] T011 [US1] Implement CLI menu option 1 for adding tasks in src/todo_app.py
- [x] T012 [US1] Add input validation for empty/whitespace-only task descriptions in src/todo_app.py
- [x] T013 [US1] Add error handling and user feedback for add task operation in src/todo_app.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Implement ability to display all tasks with their ID, description, and completion status

**Independent Test**: Can be fully tested by adding tasks and then viewing the list to confirm all tasks are displayed correctly with proper formatting.

### Implementation for User Story 2

- [x] T014 [P] [US2] Implement TaskList.get_all_tasks() method in src/todo_app.py
- [x] T015 [US2] Implement CLI menu option 2 for viewing task list in src/todo_app.py
- [x] T016 [US2] Add proper formatting for displaying tasks (ID, description, completion status) in src/todo_app.py
- [x] T017 [US2] Add handling for empty task list scenario with appropriate message in src/todo_app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: Implement ability to modify the description of an existing task by ID

**Independent Test**: Can be fully tested by updating task descriptions and confirming the changes are reflected when viewing the task list.

### Implementation for User Story 3

- [x] T018 [P] [US3] Implement TaskList.update_task() method for changing task descriptions in src/todo_app.py
- [x] T019 [US3] Implement CLI menu option 3 for updating tasks in src/todo_app.py
- [x] T020 [US3] Add validation to ensure task ID exists before updating in src/todo_app.py
- [x] T021 [US3] Add input validation for empty/whitespace-only new descriptions in src/todo_app.py
- [x] T022 [US3] Add error handling for invalid task IDs during update in src/todo_app.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Implement ability to remove tasks from the list by ID

**Independent Test**: Can be fully tested by deleting tasks and confirming they no longer appear in the task list.

### Implementation for User Story 4

- [x] T023 [P] [US4] Implement TaskList.delete_task() method in src/todo_app.py
- [x] T024 [US4] Implement CLI menu option 4 for deleting tasks in src/todo_app.py
- [x] T025 [US4] Add validation to ensure task ID exists before deletion in src/todo_app.py
- [x] T026 [US4] Add error handling for invalid task IDs during deletion in src/todo_app.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete / Incomplete (Priority: P2)

**Goal**: Implement ability to track task completion by marking tasks as complete or incomplete by ID

**Independent Test**: Can be fully tested by marking tasks as complete/incomplete and confirming the status changes are reflected in the task list.

### Implementation for User Story 5

- [x] T027 [P] [US5] Implement TaskList.mark_task_completed() method in src/todo_app.py
- [x] T028 [US5] Implement TaskList.mark_task_incomplete() method in src/todo_app.py
- [x] T029 [US5] Implement CLI menu option 5 for marking tasks complete in src/todo_app.py
- [x] T030 [US5] Implement CLI menu option 6 for marking tasks incomplete in src/todo_app.py
- [x] T031 [US5] Add validation to ensure task ID exists before marking in src/todo_app.py
- [x] T032 [US5] Add error handling for invalid task IDs during marking in src/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T033 [P] Add comprehensive error handling across all operations in src/todo_app.py
- [x] T034 [P] Improve user interface and messaging consistency in src/todo_app.py
- [x] T035 [P] Add input sanitization and validation across all user inputs in src/todo_app.py
- [x] T036 [P] Refactor code for better readability and maintainability in src/todo_app.py
- [x] T037 [P] Add docstrings and comments to explain functionality in src/todo_app.py
- [x] T038 [P] Run quickstart validation to ensure application works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with other stories but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence