#!/usr/bin/env python3
"""
Demo script to show the todo application functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app import Task, TaskList

def demo():
    print("=== Todo Application Demo ===\n")

    # Create a task list
    task_list = TaskList()

    # Add some tasks
    print("1. Adding tasks...")
    task_id1 = task_list.add_task("Learn Python")
    print(f"   Added task: ID {task_id1} - Learn Python")

    task_id2 = task_list.add_task("Build a todo app")
    print(f"   Added task: ID {task_id2} - Build a todo app")

    task_id3 = task_list.add_task("Write tests")
    print(f"   Added task: ID {task_id3} - Write tests")

    print()

    # View all tasks
    print("2. Viewing all tasks...")
    tasks = task_list.get_all_tasks()
    for task in tasks:
        # Handle the Unicode characters by replacing them for Windows compatibility
        task_str = str(task)
        task_str = task_str.replace("○", "O").replace("✓", "X")
        print(f"   {task_str}")
    print()

    # Mark a task as complete
    print(f"3. Marking task {task_id2} as complete...")
    task_list.mark_task_completed(task_id2)
    print(f"   Task {task_id2} marked as complete")
    print()

    # View tasks again to see the change
    print("4. Viewing tasks after marking one as complete...")
    tasks = task_list.get_all_tasks()
    for task in tasks:
        # Handle the Unicode characters by replacing them for Windows compatibility
        task_str = str(task)
        task_str = task_str.replace("○", "O").replace("✓", "X")
        print(f"   {task_str}")
    print()

    # Update a task
    print(f"5. Updating task {task_id1}...")
    task_list.update_task(task_id1, "Master Python")
    print(f"   Task {task_id1} updated to 'Master Python'")
    print()

    # View tasks again
    print("6. Viewing tasks after update...")
    tasks = task_list.get_all_tasks()
    for task in tasks:
        # Handle the Unicode characters by replacing them for Windows compatibility
        task_str = str(task)
        task_str = task_str.replace("○", "O").replace("✓", "X")
        print(f"   {task_str}")
    print()

    # Delete a task
    print(f"7. Deleting task {task_id3}...")
    task_list.delete_task(task_id3)
    print(f"   Task {task_id3} deleted")
    print()

    # View final tasks
    print("8. Final task list...")
    tasks = task_list.get_all_tasks()
    if tasks:
        for task in tasks:
            # Handle the Unicode characters by replacing them for Windows compatibility
            task_str = str(task)
            task_str = task_str.replace("○", "O").replace("✓", "X")
            print(f"   {task_str}")
    else:
        print("   No tasks remaining")
    print()

    print("Demo completed successfully!")

if __name__ == "__main__":
    demo()