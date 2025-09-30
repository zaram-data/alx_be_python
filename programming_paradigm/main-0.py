# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Start a new account with $100 so we can try stuff quickly
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    arg = sys.argv[1]
    if ':' in arg:
        command, param = arg.split(':', 1)
        try:
            amount = float(param)
        except ValueError:
            print("Invalid amount. Please provide a number.")
            sys.exit(1)
    else:
        command = arg
        amount = None

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print("Error:", e)
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print("Error:", e)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
