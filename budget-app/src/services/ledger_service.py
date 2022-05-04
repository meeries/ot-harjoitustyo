from repositories.ledger_repository import LedgerRepository


class LedgerService:
    def __init__(self):
        self.ledger_repository = LedgerRepository()

    def deposit(self, amount, category):
        self.ledger_repository.add_transaction(amount, category)

    def withdrawal(self, amount, category):
        if self.get_balance() - int(amount) > 0:
            self.ledger_repository.add_transaction(amount, category)
        else:
            return "Not enough balance for withdrawal."

    def get_balance(self):
        return int(self.ledger_repository.get_balance()[0])

    def check_ledger(self):
        return [dict(x) for x in self.ledger_repository.find_all()]