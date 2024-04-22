from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# this is a comment from a second developer :)
## este es un comentario de un desarrollador 1 :)

# In-memory data structure for tasks
data = {
    "tareas": [
        {
            "id": 1,
            "titulo": "Tarea 1",
            "descripcion": "Descripción de la tarea 1",
            "usuario_id": 1111
        },
        {
            "id": 2,
            "titulo": "Tarea 2",
            "descripcion": "Descripción de la tarea 2",
            "usuario_id": 2222
        }
    ]
}

@app.route("/")
def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    return "Hello World!"

# Route to get all tasks
@app.route("/tareas", methods=["GET"])
def get_all_tasks():
    return jsonify(data["tareas"])

# Route to get a specific task by ID
@app.route("/tareas/<int:tarea_id>", methods=["GET"])
def get_task_by_id(tarea_id):
    task = [t for t in data["tareas"] if t["id"] == tarea_id]
    if not task:
        abort(404, message=f"Task with ID {tarea_id} not found")

    return jsonify(task[0])

# Route to create a new task
@app.route("/tareas", methods=["POST"])
def create_task():
    if not request.is_json:
        abort(400, message="Content must be JSON")

    new_task = request.get_json()
    if not new_task or "titulo" not in new_task or "descripcion" not in new_task:
        abort(400, message="Missing required fields: titulo and descripcion")

    # Generate a new unique ID
    new_task["id"] = max([t["id"] for t in data["tareas"]]) + 1

    data["tareas"].append(new_task)
    return jsonify(new_task), 201

# Route to update an existing task
@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def update_task(tarea_id):
    if not request.is_json:
        abort(400, message="Content must be JSON")

    task = [t for t in data["tareas"] if t["id"] == tarea_id]
    if not task:
        abort(404, message=f"Task with ID {tarea_id} not found")

    updated_task = request.get_json()
    if not updated_task or "titulo" not in updated_task or "descripcion" not in updated_task:
        abort(400, message="Missing required fields: titulo and descripcion")

    task[0]["titulo"] = updated_task["titulo"]
    task[0]["descripcion"] = updated_task["descripcion"]

    return jsonify(task[0])

# Route to delete a task
@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def delete_task(tarea_id):
    task = [t for t in data["tareas"] if t["id"] == tarea_id]
    if not task:
        abort(404, message=f"Task with ID {tarea_id} not found")

    data["tareas"].remove(task[0])
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
