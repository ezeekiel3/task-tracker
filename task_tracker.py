import argparse
import json
from datetime import date

try:
    with open('datos.json', 'r') as file:
        task_arr = json.load(file)
except:
    print('El archivo esta vacio... inicializando')
    with open('datos.json', 'w') as file:
        file.write('{''"tasks": []}')

def add_task(description):
    today = date.today()

    if (len(task_arr["tasks"]) == 0):
        new_id = 0
    else:
        new_id = task_arr["tasks"][-1]["id"] + 1

    task = {
        "id": new_id,
        "description": description,
        "createdAt": str(today)
    }

    task_arr["tasks"].append(task)

    with open('datos.json', 'w') as file:
        json.dump(task_arr, file, indent=4)

parser = argparse.ArgumentParser(prog='task-cli')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description', type=str)