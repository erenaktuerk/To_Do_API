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

    def to_dict(self):
        # Convert the TodoItem object to a dictionary
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }