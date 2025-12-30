#!/usr/bin/env python3
"""
Simple test to validate the todo application functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from todo_app import Task, TaskList

def test_task_creation():
    """Test basic task creation"""
    task = Task(id=1, description="Test task", completed=False)
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed == False
    print("OK Task creation test passed")

def test_task_list_operations():
    """Test basic task list operations"""
    task_list = TaskList()

    # Test adding a task
    task_id = task_list.add_task("Test task")
    assert task_id == 1
    assert len(task_list.tasks) == 1
    print("OK Task addition test passed")

    # Test getting all tasks
    tasks = task_list.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].description == "Test task"
    print("OK Get all tasks test passed")

    # Test updating a task
    task_list.update_task(1, "Updated task")
    assert task_list.tasks[1].description == "Updated task"
    print("OK Task update test passed")

    # Test marking complete
    task_list.mark_task_completed(1)
    assert task_list.tasks[1].completed == True
    print("OK Mark complete test passed")

    # Test marking incomplete
    task_list.mark_task_incomplete(1)
    assert task_list.tasks[1].completed == False
    print("OK Mark incomplete test passed")

    # Test deleting a task
    task_list.delete_task(1)
    assert len(task_list.tasks) == 0
    print("OK Task deletion test passed")

def test_error_handling():
    """Test error handling"""
    task_list = TaskList()

    # Test adding empty task
    try:
        task_list.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("OK Empty task validation test passed")

    # Test updating with empty description
    task_list.add_task("Test task")
    try:
        task_list.update_task(1, "")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("OK Empty update validation test passed")

    # Test operations on non-existent task
    try:
        task_list.get_task_by_id(999)
        assert False, "Should have raised KeyError"
    except KeyError:
        print("OK Non-existent task validation test passed")

if __name__ == "__main__":
    print("Running todo application tests...")
    test_task_creation()
    test_task_list_operations()
    test_error_handling()
    print("All tests passed! OK")