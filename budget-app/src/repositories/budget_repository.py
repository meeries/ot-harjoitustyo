
class Budget:
    def __init__(self, balance):
        self.balance = balance
        self.ledger = []

    def deposit(self, amount, category):
        self.balance += int(amount)
        self.ledger.append({"amount": int(amount), "category": category})

    def withdrawal(self, amount, category):
        if self.balance - int(amount) > 0:
            self.balance -= int(amount)
            self.ledger.append({"amount": -int(amount), "category": category})
        else:
            return "Not enough balance for withdrawal."

    def get_balance(self):
        return {self.balance}

    def check_ledger(self):
        return self.ledger

if __name__ == "__main__":
    testaaja = Budget(0)
    testaaja.deposit(100, "salary")
    print(testaaja.ledger)
    print(testaaja.balance)