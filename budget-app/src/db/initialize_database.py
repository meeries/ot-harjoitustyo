from db import database_connection 

def create_tables_if_not_exists(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table if not exists ledger (
            id integer primary key autoincrement,
            amount integer,
            category text
        );
    ''')

    connection.commit()


def initialize_database():
    connection = database_connection.get_database_connection()
    create_tables_if_not_exists(connection)