from unicodedata import category
from repositories.budget_repository import Budget

budget = Budget(0)

COMMANDS = {
    "x": "exit",
    "d": "make deposit",
    "w": "make withdrawal",
    "l": "check ledger",
    "b": "check budget"
}

while True:
    com = input("give command: (d = deposit, w = withdrawal, b = view your current budget l = view your current ledger x = exit.)")
    if not com in COMMANDS:
        print("Invalid command.")
    if com == "d":
        x, y = input("give your deposit amount and category(e.g. 100 salary): ").split(" ", maxsplit=1)
        budget.deposit(x, y)
        print(f"deposit added!")

    elif com == "w":
        x, y = input("give your withdrawal amount and category(e.g. 20 food): ").split(" ", maxsplit=1)
        budget.withdrawal(x, y)
        print(f"wihdrawal added!")

    elif com == "b":
        print(f"your current budget is: {budget.balance}")

    elif com == "l":
        print(f"Your current ledger: {budget.ledger}")

    elif com == "x":
        print("Have a nice day! :)")
        break