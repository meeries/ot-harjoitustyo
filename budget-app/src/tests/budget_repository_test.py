import unittest
from repositories.budget_repository import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget(0)

    def test_deposit_works(self):
        self.budget.deposit(1000, "Salary")
        self.assertEqual(self.budget.balance, 1000)

    def test_withdrawal_works(self):
        self.budget.deposit(1000, "Salary")
        self.budget.withdrawal(100, "gas")
        self.assertEqual(self.budget.balance, 900)

    def test_ledger_works(self):
        self.budget.deposit(100, "salary")
        self.budget.check_ledger()
        self.assertEqual(self.budget.ledger, [{'amount': 100, 'category': 'salary'}])

    def test_get_balance_works(self):
        self.budget.deposit(100, "salary")
        self.budget.get_balance()
        self.assertEqual(self.budget.balance, 100)

    def test_withdrawal_doesnt_work_if_negative(self):
        self.budget.deposit(100, "salary")
        self.budget.withdrawal(200, "food")
        self.assertEqual(self.budget.balance, 100)