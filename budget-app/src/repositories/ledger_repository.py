from db import database_connection

class LedgerRepository:
    def __init__(self):
        self.connection = database_connection.get_database_connection()
        self.cursor = self.connection.cursor()

    def find_all(self):
        return self.cursor.execute('select * from ledger').fetchall()

    def add_transaction(self, amount, category):
        self.cursor.execute('insert into ledger values (?,?,?)', (None, amount, category))
        self.connection.commit()
    
    def get_balance(self):
        return self.cursor.execute('select sum(amount) from ledger').fetchone()