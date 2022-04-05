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