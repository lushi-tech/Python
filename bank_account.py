class BankAccount:
    # Constructor to initialize a new bank account with an account number, owner, and optional initial balance
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number  # Unique identifier for the bank account
        self.owner = owner  # Name of the account owner
        self.balance = balance  # Initial balance, default is 0.0

    # Method to deposit an amount into the account
    def deposit(self, amount):
        if amount > 0:  # Ensure the deposit amount is positive
            self.balance += amount  # Increase the account balance by the deposit amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Deposit failed. Amount must be positive."  # Return error message instead of raising an exception

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        # Check if the withdrawal amount is positive and less than or equal to the current balance
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Reduce the account balance by the withdrawal amount
            return f"Withdrawal successful. New balance: {self.balance}"
        elif amount > self.balance:  # If withdrawal amount exceeds the balance
            return "Withdrawal failed. Insufficient funds."  # Return error message instead of raising an exception
        else:
            return "Withdrawal failed. Amount must be positive."  # Return error message instead of raising an exception

    # Method to get the details of the account as a dictionary
    def get_details(self):
        return {
            "Account Number": self.account_number,  # Include the account number
            "Owner": self.owner,  # Include the owner's name
            "Balance": self.balance  # Include the current account balance
        }