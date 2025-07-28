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
        "status": "todo",
        "createdAt": str(today)
    }

    task_arr["tasks"].append(task)

    with open('datos.json', 'w') as file:
        json.dump(task_arr, file, indent=4)

def update_task(item_id, new_description):
    select_item_by_id = task_arr["tasks"][item_id]
    
    today = date.today()
    select_item_by_id["description"] = new_description
    select_item_by_id["updatedAt"] = str(today)

    with open('datos.json', 'w') as file:
        json.dump(task_arr, file, indent=4)

def delete_task(task_id):
    for i, task in enumerate(task_arr["tasks"]):
        if (task["id"] == task_id):
            del task_arr["tasks"][i]
            
            with open('datos.json', 'w') as file:
                json.dump(task_arr, file, indent=4)
            return
    print("no se encontro la tarea con el id: ", task_id)

def task_in_progress(task_id):
    for i, task in enumerate(task_arr["tasks"]):
        if (task["id"] == task_id):
            select_item_by_id = task_arr["tasks"][i]
    select_item_by_id["status"] = "in-progress"
    
    with open('datos.json', "w") as file:
        json.dump(task_arr, file, indent=4)

def task_done(task_id):
    for i, task in enumerate(task_arr["tasks"]):
        if (task["id"] == task_id):
            select_item_by_id = task_arr["tasks"][i]
    
    select_item_by_id["status"] = "done"
    with open('datos.json', "w") as file:
        json.dump(task_arr, file, indent=4)

def show_list(status=""):
    if (status == "done"):
        task_done_founded = False
        for task in task_arr["tasks"]:
            if (task["status"] == "done"):
                task_done_founded = True
                print(task)
        if (task_done_founded):
            return
        else:
            print('no se encontro ninguna tarea terminada')
            return
    
    if (status == "in-progress"):
        task_progress_founded = False
        for task in task_arr["tasks"]:
            if (task["status"] == "in-progress"):
                task_progress_founded = True
                print(task)
        if (task_progress_founded):
            return
        else:
            print('no se encontro ninguna tarea en progreso')
            return
    
    if (status == "todo"):
        task_todo_founded = False
        for task in task_arr["tasks"]:
            if (task["status"] == "todo"):
                task_todo_founded = True
                print(task)
        if (task_todo_founded):
            return
        else:
            print('no se encontro ninguna tarea para hacer')
            return

    for task in task_arr["tasks"]:
        print(task)
    

parser = argparse.ArgumentParser(prog='task-cli')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description', type=str)

update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int)
update_parser.add_argument('description', type=str)

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id', type=int)

progress_parser = subparsers.add_parser('mark-in-progress')
progress_parser.add_argument('id', type=int)

done_parser = subparsers.add_parser('mark-done')
done_parser.add_argument('id', type=int)

show_list_parser = subparsers.add_parser('list')
show_list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'])

args = parser.parse_args()

match args.command:
    case 'add':
        add_task(args.description)
    case 'update':
        update_task(args.id, args.description)
    case 'delete':
        delete_task(args.id)
    case 'mark-in-progress':
        task_in_progress(args.id)
    case 'mark-done':
        task_done(args.id)
    case 'list':
        show_list(args.status)
    case _:
        parser.print_help()