"""
File: account.py

Description: bank simulator
"""


class InsufficientFunds(Exception):
    """
        User-defined exception for signaling a banking application specific issue
    """
    def __init__(self, balance, amount):
        super().__init__(f'Insufficient funds: Balance: {balance}, Requested: {amount}')
        self.balance = balance
        self.amount = amount

    def overage(self):
        return self.balance - self.amount


class Account:

    def __init__(self, starting_balance: float):
        self.balance: float = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        # assert (self.balance >= amount), 'Insufficient balance'
        # assert (self.balance - amount >= 500), 'Minimum balance not maintained'
        if self.balance < amount:
            raise InsufficientFunds(self.balance, amount)

        self.balance -= amount

    def get_balance(self):
        return self.balance

