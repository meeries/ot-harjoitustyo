from repositories.ledger_repository import LedgerRepository

class LedgerService:
    def __init__(self):
        self.ledger_repository = LedgerRepository()

    def deposit(self, amount, category):
        if int(amount) >= 0:
            self.ledger_repository.add_transaction(amount, category)
            print("Deposit added!")
        else:
            print("Please insert a positive number")

    def withdrawal(self, amount, category):
        if int(amount) >= 0:
            if self.get_balance() - int(amount) > 0:
                self.ledger_repository.add_transaction(-int(amount), category)
                print("Withdrawal added!")
            else:
                print("Not enough balance for withdrawal.")
        else:
            print("Please insert a positive number")

    def get_balance(self):
        return int(self.ledger_repository.get_balance()[0])

    def check_ledger(self):
        return [dict(x) for x in self.ledger_repository.find_all()]

    def delete_database(self):
        self.ledger_repository.delete_db()

    #def delete_database(connection):
    #    cursor = connection.cursor()
    #    cursor.execute('''
    #        drop table ledger;
    #        ''')
    #    connection.commit()