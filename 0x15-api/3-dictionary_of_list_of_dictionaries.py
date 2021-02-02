#!/usr/bin/python3
""" REST API employee"""
from sys import argv, exit
from json import loads, dump
from requests import get


url = "https://jsonplaceholder.typicode.com/todos/"
url_us = "https://jsonplaceholder.typicode.com/users/"

tasks = []
# id_emp = argv[1]
res_user = get(url_us)
dict_us = {}


# try:
#     int(id_emp)
# except ValueError:
#     print("Must be an integer")
#     exit()

# if res_user.status_code != 200:
#     print("User error")
#     exit()

req_all = get(url)
users = loads(res_user.text)
for user in users:
    id_emp = user["id"]
    dict_us["{}".format(id_emp)] = []
    for task in loads(req_all.text):
        if task['userId'] == int(id_emp):
            dict_us[str(id_emp)].append(dict(
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user['username']
                }))
    with open('todo_all_employees.json', mode='w') as f:
        dump(dict_us, f)
