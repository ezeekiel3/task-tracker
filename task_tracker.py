import argparse
import json

def add_task(description):
    with open('datos.json', 'r') as file:
        if (file.read() == ""):
            print("El archivo esta vacio... Creando un array con el elemento")
            contenido_vacio = True
        else:
            print("El archivo no esta vacio, agregando elemento")
            contenido_vacio = False

    with open('datos.json' 'w') as file:
        if contenido_vacio:
            file.write("[]")

parser = argparse.ArgumentParser(prog="task-cli")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser('add')
add_parser.add_argument("description", type=str)