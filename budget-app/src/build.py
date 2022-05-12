from db.initialize_database import initialize_database, drop_tables


def build():
    drop_tables()
    initialize_database()

if __name__ == '__main__':
    build()
