#!/usr/bin/python3
""" REST API employee"""
from sys import argv, exit
from json import loads, dump
from requests import get


url = "https://jsonplaceholder.typicode.com/todos/"
url_us = "https://jsonplaceholder.typicode.com/users/"

if len(argv) >= 2:
    tasks_comp = 0
    tasks_tot = 0
    tasks = []
    id_emp = argv[1]
    res_user = get(url_us + id_emp)
    dict_us = {}
    dict_us["{}".format(id_emp)] = []

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
            dict_us[str(id_emp)].append(dict(
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user['username']
                }))
    with open('{}.json'.format(id_emp), mode='w') as f:
        dump(dict_us, f)
