from repositories.budget_repository import Budget

budget = Budget(0)
deposit = int(input("Make deposit: "))
withdrawal = int(input("Make withdrawal: "))
print(f"Your budget is {budget.balance+deposit-withdrawal}")