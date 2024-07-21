from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            if bank.create_account(account_number, name, initial_balance):
                print("Account created successfully.")
            else:
                print("Account with this number already exists.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if bank.deposit(account_number, amount):
                print("Amount deposited successfully.")
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if bank.withdraw(account_number, amount):
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance or account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            balance = bank.get_balance(account_number)
            if balance is not None:
                print(f"Current balance: {balance}")
            else:
                print("Account not found.")
        
        elif choice == '5':
            account_number = input("Enter account number: ")
            details = bank.get_account_details(account_number)
            if details is not None:
                print(f"Account Details: {details}")
            else:
                print("Account not found.")
        
        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
