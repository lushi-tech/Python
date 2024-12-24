
import os  # Import the os module to check if a file exists
from bank_account import BankAccount  # Import the BankAccount class from the corresponding file

# Name of the file where account data will be stored
DATA_FILE = "accounts_data.txt"

# Function to save a list of account objects to a file
def save_accounts(accounts):
    """
    This function saves the details of all accounts to a file named accounts_data.txt.
    Each account is written on a separate line in the format:
    account_number,owner,balance
    """
    with open(DATA_FILE, 'w') as file:  # Open the file in write mode ('w'), overwriting any existing data
        for account in accounts:  # Iterate through each account in the list
            # Write the account details as a single line, separated by commas
            file.write(f"{account.account_number},{account.owner},{account.balance}\n")

# Function to load account data from a file
def load_accounts():
    """
    This function reads account data from the accounts_data.txt file and recreates a list of BankAccount objects.
    If the file does not exist, it returns an empty list.
    """
    accounts = []  # Initialize an empty list to store account objects
    if os.path.exists(DATA_FILE):  # Check if the file exists using os.path.exists
        with open(DATA_FILE, 'r') as file:  # Open the file in read mode ('r')
            for line in file:  # Read each line in the file
                # Split the line by commas to get individual account details
                account_number, owner, balance = line.strip().split(',')
                # Create a BankAccount object using the extracted details and add it to the list
                accounts.append(BankAccount(account_number, owner, float(balance)))
    return accounts  # Return the list of loaded account objects