from db.initialize_database import initialize_database, drop_tables
from db.database_connection import connection


def build():
    drop_tables(connection)
    initialize_database()

if __name__ == '__main__':
    build()
