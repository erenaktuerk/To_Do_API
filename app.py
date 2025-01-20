from flask import Flask
from flask_migrate import Migrate
from app.routes import todo_routes  # Import the blueprint for the To-Do routes
from app.models import db
from flask.cli import FlaskGroup

# Create the Flask application
app = Flask(__name__)

# Load configuration from the Settings class in config.py
app.config.from_object('config.Settings')  # Make sure the settings are loaded correctly

# Initialize the database with the app
db.init_app(app)

# Initialize Flask-Migrate for handling database migrations
migrate = Migrate(app, db)

# Register the Blueprint for To-Do routes with the URL prefix '/api/todos'
app.register_blueprint(todo_routes, url_prefix='/api/todos')

# Base route for the main entry point
@app.route("/")
def index():
    return {"message": "Welcome to the To-Do API! Use /api/todos to interact with the API."}

# Route for handling favicon requests (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response for the favicon request

# Set up Flask CLI commands
cli = FlaskGroup(app)

# Run the application using the Flask CLI (useful for development)
if __name__ == '__main__':
    cli()