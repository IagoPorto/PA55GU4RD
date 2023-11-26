from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/passguard/paswords/alls', methods=['GET'])
def get_all_passwords():
    return

@app.route('/passguard/paswords/<int:pass_id>', methods=['GET'])
def get_password():
    return  

# POST request to add a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'The request must contain a title'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# PUT request to update a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    if 'title' in request.json:
        task['title'] = request.json['title']
    if 'done' in request.json:
        task['done'] = request.json['done']

    return jsonify({'task': task})

# DELETE request to delete a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    tasks.remove(task)
    return jsonify({'result': True})