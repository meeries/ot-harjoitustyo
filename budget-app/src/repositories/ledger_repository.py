from db import database_connection
from db import initialize_database

class LedgerRepository:
    def __init__(self):
        self.connection = database_connection.get_database_connection()
        self.cursor = self.connection.cursor()

    def find_all(self):
        initialize_database.initialize_database()
        return self.cursor.execute('select * from ledger').fetchall()

    def add_transaction(self, amount, category):
        initialize_database.initialize_database()
        self.cursor.execute('insert into ledger values (?,?,?)', (None, amount, category))
        self.connection.commit()
    
    def get_balance(self):
        return self.cursor.execute('select sum(amount) from ledger').fetchone()

    def delete_db(self):
        self.cursor.execute('drop table if exists ledger')
