from flask import Flask, jsonify, request

app = Flask(__name__)

base_url = "/passguard/"

@app.route(base_url + 'paswords/all', methods=['GET'])
def get_all_passwords():
    #TODO make the function
    #function that returns all the user passwords
    return

@app.route(base_url + 'paswords/<int:pass_id>', methods=['GET'])
def get_password():
    #TODO make the function
    #Function that returns a password for a specific user
    return  

@app.route(base_url + 'new', methods=['POST'])
def new_password():
    #TODO make the function
    #create a function that creats a new password for a specific service
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'The request must contain a title'}), 400

    new_pass = {
        'user': request.json['user'],
        'service': request.json['service']
    }
    return jsonify({}), 201
@app.route(base_url + 'passwords/<int:pass_id>', methods=['PUT'])

def update_password(pass_id):
    #TODO make the function
    #function that updates an especific password for a specific user

    return jsonify({})

@app.route(base_url + 'passwords/<int:pass_id>', methods=['DELETE'])
def delete_task(task_id):
    #TODO make the function
    #function that delets an especific password for an especific user
    return jsonify({})