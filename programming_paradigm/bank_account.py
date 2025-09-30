# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Make a new BankAccount. initial_balance is how much money it starts with.
        We store the balance in _account_balance (the underscore means 'keep this inside the object').
        """
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """Put money into the account. Reject negative amounts."""
        amount = float(amount)
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self._account_balance += amount
        return self._account_balance

    def withdraw(self, amount):
        """
        Try to take money out.
        If there is enough money, subtract it and return True.
        If not enough money, do nothing and return False.
        """
        amount = float(amount)
        if amount < 0:
            raise ValueError("Withdraw amount must be non-negative.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Show the current balance nicely."""
        print(f"Current Balance: ${self._account_balance:.2f}")
