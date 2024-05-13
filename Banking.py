class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.password = None

    def set_password(self, password):
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    account_number = input("Enter your account number: ")
    account_holder = input("Enter your account holder name: ")


    account1 = BankAccount(account_number, account_holder, 1000)
    account1.set_password("mysecret")  # Set a password for the account

    print(f"Welcome, {account1.account_holder}!")
    print(f"Account number: {account1.account_number}")
    print(f"Initial balance: ${account1.get_balance()}")


    entered_password = input("Enter your account password: ")
    if entered_password == account1.password:
        amount_to_deposit = float(input("Enter the amount to deposit: $"))
        account1.deposit(amount_to_deposit)

        amount_to_withdraw = float(input("Enter the amount to withdraw: $"))
        account1.withdraw(amount_to_withdraw)
    else:
        print("Incorrect password. Access denied.")

