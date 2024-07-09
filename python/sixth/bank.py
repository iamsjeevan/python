class SavingsAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposit of ${amount} successful. Current balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds. Cannot withdraw.")
        self.balance -= amount
        print(f"Withdrawal of ${amount} successful. Current balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Current balance in account {self.account_number}: ${self.balance}")

# Example usage:
try:
    # Create a savings account
    savings_acc = SavingsAccount(1001, "John Doe", 500)

    # Deposit some amount
    savings_acc.deposit(100)

    # Withdraw some amount
    savings_acc.withdraw(50)

    # Check balance
    savings_acc.check_balance()

    # Attempt to withdraw more than balance
    savings_acc.withdraw(600)

except ValueError as ve:
    print(f"Error: {ve}")
