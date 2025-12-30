# Data Model: Phase I - In-Memory Console Todo Application

## Task Entity

**Definition**: Represents a single todo item in the application

**Attributes**:
- `id` (integer): Unique sequential identifier for the task
- `description` (string): Text description of the task
- `completed` (boolean): Completion status of the task (True = completed, False = pending)

**Constraints**:
- `id` must be unique within the application session
- `id` must be a positive integer
- `description` must not be empty or whitespace-only
- `completed` defaults to False when creating a new task

**State Transitions**:
- Creation: `completed` = False
- Mark Complete: `completed` = True
- Mark Incomplete: `completed` = False

## TaskList Collection

**Definition**: In-memory collection that manages all Task entities

**Operations**:
- `add_task(description: str) -> int`: Creates a new task with unique ID and returns the ID
- `get_all_tasks() -> List[Task]`: Returns all tasks in the collection
- `get_task_by_id(task_id: int) -> Task`: Returns a specific task or raises error if not found
- `update_task(task_id: int, new_description: str) -> bool`: Updates task description, returns success status
- `delete_task(task_id: int) -> bool`: Removes task from collection, returns success status
- `mark_task_completed(task_id: int) -> bool`: Sets task completion status to True, returns success status
- `mark_task_incomplete(task_id: int) -> bool`: Sets task completion status to False, returns success status

**Constraints**:
- All operations must validate task existence before modification
- IDs must remain sequential with no gaps after deletions
- Collection must maintain data integrity during all operations

## Application State

**Definition**: Container for the current application state

**Attributes**:
- `tasks` (dict): Dictionary mapping task IDs to Task objects
- `next_id` (int): Counter for generating the next unique task ID