from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            return False
        new_account = Account(account_number, name, initial_balance)
        self.accounts[account_number] = new_account
        return True

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        return None

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_details()
        return None
