import os

class Settings:
    SECRET_KEY = os.urandom(24).hex()  # key for safety
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'  # SQLite-database im project structure
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # deactivate warnings
    DEBUG = True  # activate debug mode
    JSON_SORT_KEYS = False  # keep json key series