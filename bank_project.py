class Account:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: {amount}\nRemaining Balance: {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Amount withdrawn: {amount} | Remaining balance: {self.balance}')
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self.balance

    def get_mini_statement(self):
        print("Mini Statement:")
        print(f'Username: {self.username}')
        print(f'Current balance: {self.balance}')

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("Account Created Successfully")
            print("------- Welcome to State Bank of India -------")

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Success")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid Username")
        return None

# Main program loop
bank = BankingSystem()

while True:
    print("\n1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        bank.create_account(username, password)

    elif choice == '2':
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        account = bank.login(username, password)
        
        if account:
            while True:
                print("\n------- Welcome to State Bank of India -------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Logout")
                sub_choice = input("Enter your choice (1-5): ")

                if sub_choice == '1':
                    try:
                        amount = int(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    except ValueError:
                        print("Please enter a valid number.")

                elif sub_choice == '2':
                    try:
                        amount = int(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    except ValueError:
                        print("Please enter a valid number.")

                elif sub_choice == '3':
                    print(f'Current balance: {account.get_balance()}')
                    
                elif sub_choice == '4':
                    account.get_mini_statement()

                elif sub_choice == '5':
                    print("------- Thank You. Visit Again -------")
                    break

                else:
                    print("Invalid choice")

    elif choice == '3':
        print("------- Thank You -------")
        break

    else:
        print("Invalid Choice")


        
    