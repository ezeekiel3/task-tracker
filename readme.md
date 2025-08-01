# 📝 task-cli

Un programa de línea de comandos simple para gestionar tareas, escrito en Python. Guarda las tareas en un archivo JSON (`datos.json`) y permite agregarlas, listarlas, actualizarlas, eliminarlas y cambiar su estado.

## 🚀 Cómo usar

### 📦 Requisitos

-   Python 3.7 o superior

### 📁 Estructura esperada del archivo JSON

```json
{
  "tasks": []
}

## Comandos Disponibles
# Agregar una nueva tarea
python task_tracker.py add "Read Bible"

# Actualizar una tarea por ID
python task_tracker.py update 0 "Read Bible and pray"

# Eliminar una tarea por ID
python task_tracker.py delete 0

# Marcar una tarea como "in-progress"
python task_tracker.py mark-in-progress 0

# Marcar una tarea como "done"
python task_tracker.py mark-done 0

# Listar todas las tareas
python task_tracker.py list

# Listar tareas por estado
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done

## Archivos principales
# task_tracker.py: archivo principal con toda la lógica del CLI.

# datos.json: base de datos donde se almacenan las tareas.

## Notas
```
