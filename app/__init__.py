from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import FlaskGroup  # Import FlaskGroup for CLI commands

# Initialize the Flask application and SQLAlchemy instance
app = Flask(__name__)

# Load configuration from the Settings class in config.py
app.config.from_object('config.Settings')

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Initialize Flask-Migrate for handling database migrations
migrate = Migrate(app, db)

# Import Blueprints and Models after app initialization to avoid circular imports
from app.routes import todo_routes  # Import the to-do routes blueprint
from app.models import db  # Import the db instance here to avoid circular import issues

# Register the Blueprint for the To-Do routes with the URL prefix '/api/todos'
app.register_blueprint(todo_routes, url_prefix='/api/todos')

# Main route for the API entry point
@app.route("/")
def index():
    return {"message": "Welcome to the To-Do API! Use /api/todos to interact with the API."}

# Optional route for handling favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response for favicon requests

# Initialize Flask CLI commands
cli = FlaskGroup(app)

# Run the Flask application using Flask CLI for development (i.e., flask run command)
if __name__ == '__main__':
    cli()  # Start the server with the Flask CLI