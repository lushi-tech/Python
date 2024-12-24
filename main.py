from file_handler import load_accounts, save_accounts  # Import functions to load and save accounts data
from operations import (  # Import all the operations for managing bank accounts
    create_account, delete_account, deposit_to_account, 
    withdraw_from_account, view_account_balance, list_all_accounts
)

def main():
    """
    Main function to manage the bank account system.
    Loads existing accounts from a file, displays a menu for various operations,
    and saves the updated accounts data back to the file upon exiting.
    """
    accounts = load_accounts()  # Load existing accounts from the data file into a list
    
    while True:  # Infinite loop to continuously show the menu until the user decides to exit
        # Display menu options
        print("\n=== Bank Account Management System ===")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Deposit Funds")
        print("4. Withdraw Funds")
        print("5. View Account Balance")
        print("6. List All Accounts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")  # Prompt the user to select an option
        if choice == '1':  # If the user selects '1', create a new account
            create_account(accounts)
        elif choice == '2':  # If the user selects '2', delete an existing account
            delete_account(accounts)
        elif choice == '3':  # If the user selects '3', deposit funds into an account
            deposit_to_account(accounts)
        elif choice == '4':  # If the user selects '4', withdraw funds from an account
            withdraw_from_account(accounts)
        elif choice == '5':  # If the user selects '5', view the balance of a specific account
            view_account_balance(accounts)
        elif choice == '6':  # If the user selects '6', list all accounts in the system
            list_all_accounts(accounts)
        elif choice == '7':  # If the user selects '7', exit the program
            save_accounts(accounts)  # Save the updated accounts data back to the file
            print("Goodbye!")  # Print a goodbye message
            break  # Break the loop and exit the program
        else:  # If the user enters an invalid option
            print("Invalid choice. Please try again.")  # Notify the user and show the menu again

# Entry point for the program
if __name__ == "__main__":
    main()  # Call the main function to start the program