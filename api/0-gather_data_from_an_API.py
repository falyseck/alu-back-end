#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetches and displays employee TODO list progress."""
    # API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    user_data = user_response.json()

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Filter and count tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]

    # Display the first line of progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer as employee ID.")
