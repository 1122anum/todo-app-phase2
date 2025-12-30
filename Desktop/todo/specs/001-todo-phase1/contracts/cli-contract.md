# API Contract: Todo Console Application

## CLI Interface Specification

### Core Operations

#### Add Task
- **Command**: User selects option 1 from main menu
- **Input**: Task description string
- **Validation**:
  - Description must not be empty or whitespace-only
- **Output**: Success message with assigned task ID
- **Error Cases**:
  - Empty description → Error message, no task created

#### View Task List
- **Command**: User selects option 2 from main menu
- **Input**: None
- **Output**: Formatted list of all tasks showing ID, description, and completion status
- **Error Cases**:
  - Empty task list → "No tasks available" message

#### Update Task
- **Command**: User selects option 3 from main menu
- **Input**: Task ID (integer) and new description string
- **Validation**:
  - Task ID must exist in the system
  - New description must not be empty or whitespace-only
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid task ID → Error message
  - Empty description → Error message

#### Delete Task
- **Command**: User selects option 4 from main menu
- **Input**: Task ID (integer)
- **Validation**: Task ID must exist in the system
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid task ID → Error message

#### Mark Task Complete
- **Command**: User selects option 5 from main menu
- **Input**: Task ID (integer)
- **Validation**: Task ID must exist in the system
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid task ID → Error message

#### Mark Task Incomplete
- **Command**: User selects option 6 from main menu
- **Input**: Task ID (integer)
- **Validation**: Task ID must exist in the system
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid task ID → Error message

#### Exit
- **Command**: User selects option 7 from main menu
- **Output**: Application terminates with goodbye message