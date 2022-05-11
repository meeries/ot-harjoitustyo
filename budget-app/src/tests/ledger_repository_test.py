import unittest
from repositories import ledger_repository
from db import initialize_database

class TestLedgerRepo(unittest.TestCase):
    def setUp(self):
        initialize_database.initialize_database()
        self.budget = ledger_repository.LedgerRepository()

    def test_delete_db_works(self):
        self.budget.add_transaction(100, "food")
        self.budget.delete_db()
        self.assertEqual(self.budget.find_all(), [])

    def test_transaction_works(self):
        self.budget.add_transaction(1000, "Salary")
        self.assertEqual(self.budget.get_balance()[0], 1000)
