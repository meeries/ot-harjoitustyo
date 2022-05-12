import sqlite3
from db.config import database_file_path

connection = sqlite3.connect(database_file_path)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
