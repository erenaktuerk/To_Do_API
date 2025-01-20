To-Do API Project

Overview

The To-Do API is a simple, RESTful application built with Flask that allows users to manage tasks (or to-do items). This project demonstrates how to create a basic CRUD (Create, Read, Update, Delete) API with Flask, which interacts with a SQLite database to store to-do items. It utilizes REST principles to interact with data through HTTP requests.

Core Concepts:
	•	RESTful Architecture: The API follows standard REST principles with HTTP methods (GET, POST, PUT, DELETE) to interact with resources (to-do items).
	•	Flask Framework: Lightweight Python framework used for building the API.
	•	SQLAlchemy ORM: Used to interact with the SQLite database, making it easier to handle database operations.
	•	CRUD Operations: The application allows creating, reading, and updating to-do items.
	•	JSON Data Exchange: The API communicates using JSON format for requests and responses.

Folder Structure

To_do_api/
│
├── app.py                   # Main application file
├── config.py                # Configuration settings
├── license                  # License file for the project
├── readme.md                # Project documentation
├── requirements.txt         # List of dependencies
│
├── _pycache_/             # Folder for compiled Python files
│
├── app/                     # Core application files
│   ├── _init_.py          # Initialization of the app
│   ├── models.py            # Database models
│   ├── routes.py            # API endpoints and routes
│
├── instance/                # Database files
│   ├── database.db          # Main SQLite database
│   ├── test.db              # Test database
│   ├── todos.db             # SQLite database for todos
│
├── migrations/              # Database migrations folder
│
├── scripts/                 # Helper scripts
│   ├── send_request.py      # Script to send test API requests
│   ├── update_todo.py       # Script to update todo items
│
├── venv/                    # Virtual environment folder

Installation

Follow these steps to set up and run the To-Do API project locally:
	1.	Clone the repository:

git clone https://github.com/yourusername/to_do_api.git


	2.	Navigate to the project folder:

cd to_do_api


	3.	Set up the virtual environment:

python -m venv venv


	4.	Activate the virtual environment:
	•	On Windows:

.\venv\Scripts\activate


	•	On macOS/Linux:

source venv/bin/activate


	5.	Install the dependencies:

pip install -r requirements.txt


	6.	Set up the database:
The database is automatically created when the application is run, but you can run the migrations to set it up.

flask db upgrade



Running the Application

Once everything is set up, you can run the Flask app:

flask run

The app will start and can be accessed at http://127.0.0.1:5000.

Testing the API

You can test the To-Do API using PowerShell’s Invoke-RestMethod command to perform GET, POST, and PUT requests.

POST Request (Create a To-Do Item)

To create a new to-do item, send a POST request with JSON data:

Invoke-RestMethod -Uri http://127.0.0.1:5000/api/todos/ -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"title": "Buy groceries", "description": "Buy milk, bread, and eggs."}'

GET Request (Retrieve All To-Do Items)

To retrieve all to-do items, send a GET request:

Invoke-RestMethod -Uri http://127.0.0.1:5000/api/todos/ -Method Get

PUT Request (Update a To-Do Item)

To update an existing to-do item, use a PUT request. Replace 2 with the actual to-do ID and specify the updated title and description:

Invoke-RestMethod -Uri http://127.0.0.1:5000/api/todos/2 -Method Put -Headers @{ "Content-Type" = "application/json" } -Body '{"title": "Buy groceries updated", "description": "Buy milk, bread, eggs, and cheese."}'

DELETE Request (Delete a To-Do Item)

To delete a to-do item, send a DELETE request with the ID of the item you want to delete:

Invoke-RestMethod -Uri http://127.0.0.1:5000/api/todos/2 -Method Delete

Database Models

The TodoItem model is defined in app/models.py:

from app import db  # Import the db instance from _init_.py

# Define the TodoItem model
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each Todo item
    title = db.Column(db.String(100), nullable=False)  # Title of the Todo item (required)
    description = db.Column(db.String(200))  # Optional description for the Todo item
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp for when the Todo item is created
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp for when the Todo item is updated

    def _repr_(self):
        # Return a string representation of the TodoItem instance
        return f'<TodoItem {self.title}>'

Database Structure

The SQLite database contains a table for the to-do items, with columns for:
	•	id: The unique identifier for each to-do item.
	•	title: The title of the to-do item (required).
	•	description: A description of the to-do item (optional).
	•	created_at: The timestamp when the to-do item was created.
	•	updated_at: The timestamp when the to-do item was last updated.

Files
	•	app.py: Main entry point for the application. It contains the route definitions and application logic.
	•	config.py: Configuration file for setting up the app and database.
	•	send_request.py: A script to send test API requests using requests library.
	•	update_todo.py: A script to update existing to-do items.
	•	database.db: The SQLite database that stores the to-do items.
	•	test.db: A secondary database for testing purposes.
	•	todos.db: The primary SQLite database used for the to-do app.

Dependencies

The project requires the following dependencies, which are listed in the requirements.txt file:

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
requests==2.25.1

To install them, run:

pip install -r requirements.txt

License

This project is licensed under the MIT License.