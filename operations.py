# Import the BankAccount class
from bank_account import BankAccount
import random  # To generate random account numbers

# Function to create a new bank account
def create_account(accounts):
    # Prompt user for account owner's name and initial balance
    owner = input("Enter the account owner's name: ")
    balance = float(input("Enter the initial deposit amount: "))
    
    # Generate a random 6-digit account number
    account_number = str(random.randint(100000, 999999))  # Random 6-digit account number
    
    # Create a new BankAccount instance
    new_account = BankAccount(account_number, owner, balance)
    
    # Add the new account to the accounts list
    accounts.append(new_account)
    
    # Display success message with the new account number
    print(f"Account created successfully! Account Number: {account_number}")

# Function to delete an existing bank account
def delete_account(accounts):
    # Prompt user for the account number to delete
    account_number = input("Enter the account number to delete: ")
    
    # Loop through the list of accounts and search for the matching account number
    for account in accounts:
        if account.account_number == account_number:
            # Remove the account from the list if found
            accounts.remove(account)
            print("Account deleted successfully.")
            return  # Exit function after successful deletion
    
    # If account not found
    print("Account not found.")

# Function to deposit money into an account
def deposit_to_account(accounts):
    # Prompt user for the account number to deposit money into
    account_number = input("Enter the account number: ")
    
    # Loop through the list of accounts and find the matching account
    for account in accounts:
        if account.account_number == account_number:
            # Prompt user for the deposit amount
            amount = float(input("Enter the deposit amount: "))
            try:
                # Call the deposit method of the BankAccount class
                account.deposit(amount)
                print("Deposit successful.")
            except ValueError as e:
                # Handle any errors (e.g., negative deposit amounts)
                print(e)
            return  # Exit function after successful deposit
    
    # If account not found
    print("Account not found.")

# Function to withdraw money from an account
def withdraw_from_account(accounts):
    # Prompt user for the account number to withdraw money from
    account_number = input("Enter the account number: ")
    
    # Loop through the list of accounts and find the matching account
    for account in accounts:
        if account.account_number == account_number:
            # Prompt user for the withdrawal amount
            amount = float(input("Enter the withdrawal amount: "))
            try:
                # Call the withdraw method of the BankAccount class
                account.withdraw(amount)
                print("Withdrawal successful.")
            except ValueError as e:
                # Handle any errors (e.g., insufficient funds or invalid withdrawal amount)
                print(e)
            return  # Exit function after successful withdrawal
    
    # If account not found
    print("Account not found.")

# Function to view the balance and details of an account
def view_account_balance(accounts):
    # Prompt user for the account number to view balance
    account_number = input("Enter the account number: ")
    
    # Loop through the list of accounts and find the matching account
    for account in accounts:
        if account.account_number == account_number:
            # Retrieve the account details (assumed method get_details)
            details = account.get_details()
            # Print account details
            print(f"Account Number: {details['Account Number']}")
            print(f"Owner: {details['Owner']}")
            print(f"Balance: {details['Balance']}")
            return  # Exit function after displaying account details
    
    # If account not found
    print("Account not found.")

# Function to list all existing accounts
def list_all_accounts(accounts):
    if accounts:
        # If there are accounts in the list, loop through and print their details
        for account in accounts:
            details = account.get_details()
            print(f"Account Number: {details['Account Number']}, Owner: {details['Owner']}, Balance: {details['Balance']}")
    else:
        # If there are no accounts
        print("No accounts found.")