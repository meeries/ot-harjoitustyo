from services.ledger_service import LedgerService
from db.initialize_database import initialize_database

initialize_database()

budget = LedgerService()


COMMANDS = {
    "x": "exit",
    "d": "make deposit",
    "w": "make withdrawal",
    "l": "check ledger",
    "b": "check budget",
    "r": "reset"
}

while True:
    com = input("give command: (d = deposit, w = withdrawal, b = view your current budget l = view your current ledger x = exit.)")
    if not com in COMMANDS:
        print("Invalid command.")
    if com == "d":
        x, y = input("give your deposit amount and category(e.g. 100 salary): ").split(" ", maxsplit=1)
        budget.deposit(x, y)

    elif com == "w":
        x, y = input("give your withdrawal amount and category(e.g. 20 food): ").split(" ", maxsplit=1)
        budget.withdrawal(x, y)

    elif com == "b":
        print(f"your current budget is: {budget.get_balance()}")

    elif com == "l":
        print(f"Your current ledger: {budget.check_ledger()}")

    elif com == "r":
        budget.delete_database()
        print("reset complete")

    elif com == "x":
        print("Have a nice day! :)")
        break
    