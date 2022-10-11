"""
File: account.py

Description: bank simulator
"""


class Account:

    def __init__(self, starting_balance: float):
        self.balance: float = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert (self.balance >= amount), 'Insufficient balance'
        assert (self.balance >= 500), 'Minimum balance not maintained'

        self.balance -= amount

    def get_balance(self):
        return self.balance

