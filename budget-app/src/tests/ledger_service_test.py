import unittest
from services.ledger_service import LedgerService
from db import initialize_database

class TestLedgerService(unittest.TestCase):
    def setUp(self):
        initialize_database.initialize_database()
        self.budget = LedgerService()
        self.budget.delete_database()

    def test_deposit_works(self):
        self.budget.deposit(1000, "Salary")
        self.assertEqual(self.budget.get_balance(), 1000)
        self.assertEqual(self.budget.deposit(1000, "Salary"), True)
        initialize_database.initialize_database()

    def test_deposit_doesnt_work_negative(self):
        self.budget.deposit(-10, "food")
        self.assertEqual(self.budget.get_balance(), 0)
        self.assertEqual(self.budget.deposit(-10, "food"), False)
        
    def test_withdrawal_works(self):
        self.budget.deposit(1000, "Salary")
        self.budget.withdrawal(100, "food")
        self.assertEqual(self.budget.get_balance(), 900)
        initialize_database.initialize_database()

    def test_w_doesnt_work_if_negative(self):
        self.budget.deposit(1000, "salary")
        self.budget.withdrawal(-1, "Food")
        self.assertEqual(self.budget.withdrawal(-1, "Food"), False)

    def test_ledger_works(self):
        self.budget.deposit(100, "salary")
        self.budget.check_ledger()
        self.assertEqual(self.budget.check_ledger(), [{'id': 1, 'amount': 100, 'description': 'salary'}])
        initialize_database.initialize_database()

    def test_get_balance_works(self):
        self.budget.deposit(100, "salary")
        self.budget.get_balance()
        self.assertEqual(self.budget.get_balance(), 100)
        initialize_database.initialize_database()

    def test_withdrawal_doesnt_work_if_no_balance(self):
        self.budget.deposit(100, "salary")
        self.budget.withdrawal(200, "food")
        self.assertEqual(self.budget.get_balance(), 100)
        initialize_database.initialize_database()

    def test_its_not_a_number_works(self):
        self.budget.is_it_a_number("aa")
        self.assertEqual(self.budget.is_it_a_number("aa"), False)

    def test_is_a_number_works(self):
        self.budget.is_it_a_number(3)
        self.assertEqual(self.budget.is_it_a_number(3), True)