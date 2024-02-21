#!/usr/bin/python3

"""
Python script that, using this REST API (https://jsonplaceholder.typicode.com/)
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests

def get_todo_list_progress(employee_id):
    # Base URLs for user and todo information using the `format` method for string formatting
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    
    # Fetching user information
    user_response = requests.get(users_url, verify=False)
    user_data = user_response.json()
    
    # Fetching todos information
    todos_response = requests.get(todos_url, verify=False)
    todos_data = todos_response.json()
    
    # Calculating TODO list progress
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task['completed']])
    
    # Output
    print("Employee {} is done with tasks({}/{}):".format(user_data['name'], completed_tasks, total_tasks))
    for task in todos_data:
        if task['completed']:
            print("\t {}".format(task['title']))

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_todo_list_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: python script.py <employee_id>")

