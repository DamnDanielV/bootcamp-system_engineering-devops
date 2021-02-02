#!/usr/bin/python3
""" REST API employee"""
from sys import argv, exit
from json import loads
from requests import get


url = "https://jsonplaceholder.typicode.com/todos/"
url_us = "https://jsonplaceholder.typicode.com/users/"

if len(argv) >= 2:
    tasks_comp = 0
    tasks_tot = 0
    tasks = []
    id_emp = argv[1]
    res_user = get(url_us + id_emp)

    try:
        int(id_emp)
    except ValueError:
        print("Must be an integer")
        exit()

    if res_user.status_code != 200:
        print("User error")
        exit()

    req_all = get(url)
    user = loads(res_user.text)

    for task in loads(req_all.text):
        if task['userId'] == int(id_emp):
            tasks_tot += 1
            if task["completed"]:
                tasks.append(task)
                tasks_comp += 1

    print("Employee {} is done with tasks({}/{}):".format(
            user["name"], tasks_comp, tasks_tot))

    for task in tasks:
        if task['userId'] == int(id_emp):
            print("\t{}".format(task["title"]))
