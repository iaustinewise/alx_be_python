import json

class BankAccount:
    def __init__(self, initial_balance=0):
        self._filename = "balance.json"
        try:
            with open(self._filename, 'r') as f:
                self._account_balance = json.load(f)
        except FileNotFoundError:
            self._account_balance = initial_balance
            self.save_balance()

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            self.save_balance()
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            self.save_balance()
            return True
        return False

    def display_balance(self):
        print(f"{self._account_balance:.2f}")

    def save_balance(self):
        with open(self._filename, 'w') as f:
            json.dump(self._account_balance, f)
