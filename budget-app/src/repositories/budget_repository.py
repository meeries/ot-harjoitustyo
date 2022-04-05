
class Budget:
    def __init__(self, balance):
        self.balance = balance
        self.book = []

    def deposit(self, amount, category):
        self.balance += amount
        self.book.append({amount, category})

    def withdrawal(self, amount, category):
        if self.balance - amount > 0:
            self.balance -= amount
            self.book.append({-1 * amount, category})
        else:
            return "Not enough balance for withdrawal."

    def get_balance(self):
        return {self.balance}

if __name__ == "__main__":
    testaaja = Budget(0)
    testaaja.get_balance()
    testaaja.deposit(1000, "salary")
    testaaja.withdrawal(100, "gas")
    testaaja.withdrawal(10000, "house")
    print(testaaja.balance)