from flask import Blueprint, request, jsonify
from app import db  # Import db from the app instance
from app.models import TodoItem  # Import TodoItem model from models.py

# Create a blueprint for the to-do routes
todo_routes = Blueprint('todo_routes', __name__)

# GET route to fetch all to-do items
@todo_routes.route('/', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()  # Fetch all to-do items from the database
    return jsonify([todo.to_dict() for todo in todos]), 200  # Return the list of todos in JSON format

# POST route to add a new to-do item
@todo_routes.route('/', methods=['POST'])
def add_todo():
    data = request.get_json()  # Get the JSON data from the request
    title = data.get('title')  # Extract the title from the request data
    description = data.get('description')  # Extract the description from the request data

    if not title:  # If title is missing, return an error
        return jsonify({"error": "Title is required"}), 400

    # Create a new TodoItem object
    new_todo = TodoItem(title=title, description=description)

    db.session.add(new_todo)  # Add the new to-do item to the session
    db.session.commit()  # Commit the transaction to the database

    return jsonify(new_todo.to_dict()), 201  # Return the newly created to-do item in JSON format

# PUT route to update an existing to-do item by ID
@todo_routes.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = TodoItem.query.get(id)  # Find the to-do item by its ID

    if not todo:  # If no to-do item is found, return an error
        return jsonify({"error": "Todo item not found"}), 404

    data = request.get_json()  # Get the JSON data from the request
    todo.title = data.get('title', todo.title)  # Update the title if provided
    todo.description = data.get('description', todo.description)  # Update the description if provided

    db.session.commit()  # Commit the changes to the database

    return jsonify(todo.to_dict()), 200  # Return the updated to-do item in JSON format

# DELETE route to delete a to-do item by ID
@todo_routes.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get(id)  # Find the to-do item by its ID

    if not todo:  # If no to-do item is found, return an error
        return jsonify({"error": "Todo item not found"}), 404

    db.session.delete(todo)  # Delete the to-do item from the session
    db.session.commit()  # Commit the transaction to the database

    return jsonify({"message": "Todo item deleted"}), 200  # Return a success message