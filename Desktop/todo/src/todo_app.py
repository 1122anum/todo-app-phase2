#!/usr/bin/env python3
"""
Todo Console Application - Phase I Implementation

A simple in-memory console application for managing tasks.
Features include: adding, viewing, updating, deleting, and marking tasks complete/incomplete.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo item with ID, description, and completion status.
    """
    id: int
    description: str
    completed: bool = False

    def __str__(self) -> str:
        """Return a formatted string representation of the task."""
        status = "✓" if self.completed else "○"
        return f"{self.id}. [{status}] {self.description}"


class TaskList:
    """
    In-memory collection that manages all Task entities.
    """

    def __init__(self):
        """Initialize an empty task list with next ID counter."""
        self.tasks = {}  # Dictionary mapping task IDs to Task objects
        self.next_id = 1  # Counter for generating the next unique task ID

    def add_task(self, description: str) -> int:
        """
        Creates a new task with unique ID and returns the ID.

        Args:
            description: The task description

        Returns:
            The ID of the newly created task
        """
        if not description or description.strip() == "":
            raise ValueError("Task description cannot be empty or whitespace-only")

        task_id = self.next_id
        self.tasks[task_id] = Task(id=task_id, description=description.strip())
        self.next_id += 1
        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the collection, sorted by ID.

        Returns:
            List of all tasks sorted by ID
        """
        return sorted(self.tasks.values(), key=lambda task: task.id)

    def get_task_by_id(self, task_id: int) -> Task:
        """
        Returns a specific task or raises error if not found.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task with the specified ID

        Raises:
            KeyError: If no task exists with the given ID
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")
        return self.tasks[task_id]

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Updates task description, returns success status.

        Args:
            task_id: The ID of the task to update
            new_description: The new description for the task

        Returns:
            True if the task was successfully updated, False otherwise
        """
        if not new_description or new_description.strip() == "":
            raise ValueError("Task description cannot be empty or whitespace-only")

        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        self.tasks[task_id].description = new_description.strip()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Removes task from collection, returns success status.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was successfully deleted, False otherwise
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        del self.tasks[task_id]
        return True

    def mark_task_completed(self, task_id: int) -> bool:
        """
        Sets task completion status to True, returns success status.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            True if the task was successfully marked as completed, False otherwise
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        self.tasks[task_id].completed = True
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Sets task completion status to False, returns success status.

        Args:
            task_id: The ID of the task to mark as incomplete

        Returns:
            True if the task was successfully marked as incomplete, False otherwise
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        self.tasks[task_id].completed = False
        return True


def display_menu():
    """Display the main menu options to the user."""
    print("\n=== Todo Application ===")
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print("=" * 24)


def get_user_choice() -> str:
    """
    Get and validate user's menu choice.

    Returns:
        The user's choice as a string
    """
    try:
        choice = input("\nEnter your choice (1-7): ").strip()
        return choice
    except (EOFError, KeyboardInterrupt):
        return "7"  # Treat as exit


def handle_add_task(task_list: TaskList):
    """
    Handle the add task functionality.

    Args:
        task_list: The TaskList instance to add the task to
    """
    try:
        description = input("Enter task description: ").strip()
        task_id = task_list.add_task(description)
        print(f"Task added successfully with ID: {task_id}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def handle_view_tasks(task_list: TaskList):
    """
    Handle the view task list functionality.

    Args:
        task_list: The TaskList instance to view tasks from
    """
    tasks = task_list.get_all_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        print(task)


def handle_update_task(task_list: TaskList):
    """
    Handle the update task functionality.

    Args:
        task_list: The TaskList instance to update the task in
    """
    try:
        task_id = int(input("Enter task ID to update: "))
        new_description = input("Enter new description: ").strip()
        task_list.update_task(task_id, new_description)
        print(f"Task {task_id} updated successfully.")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid task ID (number).")
        else:
            print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def handle_delete_task(task_list: TaskList):
    """
    Handle the delete task functionality.

    Args:
        task_list: The TaskList instance to delete the task from
    """
    try:
        task_id = int(input("Enter task ID to delete: "))
        task_list.delete_task(task_id)
        print(f"Task {task_id} deleted successfully.")
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def handle_mark_complete(task_list: TaskList):
    """
    Handle the mark task complete functionality.

    Args:
        task_list: The TaskList instance to mark the task as complete
    """
    try:
        task_id = int(input("Enter task ID to mark complete: "))
        task_list.mark_task_completed(task_id)
        print(f"Task {task_id} marked as complete.")
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def handle_mark_incomplete(task_list: TaskList):
    """
    Handle the mark task incomplete functionality.

    Args:
        task_list: The TaskList instance to mark the task as incomplete
    """
    try:
        task_id = int(input("Enter task ID to mark incomplete: "))
        task_list.mark_task_incomplete(task_id)
        print(f"Task {task_id} marked as incomplete.")
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    """Main application loop."""
    print("Welcome to the Todo Application!")
    task_list = TaskList()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            handle_add_task(task_list)
        elif choice == "2":
            handle_view_tasks(task_list)
        elif choice == "3":
            handle_update_task(task_list)
        elif choice == "4":
            handle_delete_task(task_list)
        elif choice == "5":
            handle_mark_complete(task_list)
        elif choice == "6":
            handle_mark_incomplete(task_list)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()