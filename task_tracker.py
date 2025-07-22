import argparse
import json
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str

def add_task(description):
    try:
        with open('datos.json', 'r') as file:
            data = json.load(file)
    except:
        print('El archivo esta vacio, inicializando...')
        with open('datos.json', 'w') as file:
            file.write("{}")

    task: Task = {
        "id": int,
        "description": description,
        "status": str
    }


parser = argparse.ArgumentParser(prog='task-cli')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description', type=str)