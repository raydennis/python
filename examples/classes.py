import unittest


class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0


class TestBankAccount(unittest.TestCase):
    def test_bank_account_deposit(self):
        account = BankAccount(0)
        account.deposit(5)
        self.assertEqual(account.balance, 5)

    def test_bank_account_withdraw(self):
        account = BankAccount(5)
        account.withdraw(5)
        self.assertEqual(account.balance, 0)

    def test_bank_account_overdrawn_true(self):
        account = BankAccount(-5)
        self.assertTrue(account.overdrawn())

    def test_bank_account_overdrawn_false(self):
        account = BankAccount(5)
        self.assertFalse(account.overdrawn())


class testIng(unittest.TestCase):
    def WhateverIWannaDo(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
