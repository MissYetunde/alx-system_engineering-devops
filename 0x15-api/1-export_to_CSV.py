#!/usr/bin/python3

"""
Python script that, using this REST API (https://jsonplaceholder.typicode.com/)
for a given employee ID, returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


def export_csv():
    """
    Function definition to retrieve data from API
    """

    # Check if Employee ID has been provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <ID>")
        sys.exit(1)

    # Base URL
    user_url = "https://jsonplaceholder.typicode.com/users"

    # Get Employee name
    response = requests.get("{}".format(user_url))
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['id'] == int(sys.argv[1]):
                user_id = user['id']
                username = user['username']

    # Get Todos status
    response = requests.get("{}/{}/todos".format(user_url, sys.argv[1]))
    if response.status_code == 200:
        todos = response.json()

    csv_data = [
            [user_id, username, todo['completed'], todo['title']]
            for todo in todos
            ]

    # Write CSV
    filename = str(user_id) + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(csv_data)


if __name__ == "__main__":
    """Function call"""
    export_csv()
