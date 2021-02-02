#!/usr/bin/python3
""" REST API employee"""
from sys import argv, exit
from json import loads
from requests import get
import csv


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
    with open('{}.csv'.format(id_emp), mode='w') as f:
        for task in loads(req_all.text):
            if task['userId'] == int(id_emp):
                USER_ID = id_emp
                USERNAME = user["username"]
                TASK_COMPLETED_STATUS = task["completed"]
                TASK_TITLE = task["title"]

                wr = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
                wr.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                            TASK_TITLE])
