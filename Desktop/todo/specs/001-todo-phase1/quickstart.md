# Quickstart Guide: Phase I - In-Memory Console Todo Application

## Running the Application

1. **Prerequisites**: Python 3.8 or higher installed on your system

2. **Execution**:
   ```bash
   python src/todo_app.py
   ```

3. **Initial State**: Application starts with an empty task list

## Using the Menu System

The application presents a menu-driven interface with the following options:

1. **Add Task**: Creates a new task with a user-provided description
2. **View Task List**: Displays all tasks with their ID, description, and completion status
3. **Update Task**: Modifies the description of an existing task by ID
4. **Delete Task**: Removes a task from the list by ID
5. **Mark Task Complete**: Changes a task's status to completed by ID
6. **Mark Task Incomplete**: Changes a task's status to pending by ID
7. **Exit**: Terminates the application

## Example Workflow

1. Launch the application
2. Select "1" to add a task and enter your task description
3. Select "2" to view your task list
4. Select other options as needed to manage your tasks
5. Select "7" to exit (note: all data is lost on exit)

## Error Handling

- Invalid task IDs will result in error messages
- Empty task lists will display appropriate messages
- Invalid menu choices will prompt for valid input
- Empty or whitespace-only task descriptions are rejected

## Development

To run tests:
```bash
pytest tests/
```

To run the application in development mode:
```bash
python src/todo_app.py
```