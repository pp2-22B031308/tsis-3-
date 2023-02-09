class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of ${amount} accepted. New balance: ${self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Not Enough Funds!')
        else:
            self.balance -= amount
            print(f'Withdrawal of ${amount} accepted. New balance is ${self.balance}')

# jon = Account('John Doe', 100)

# jon.deposit(50)
# jon.withdraw(150)
# jon.withdraw(75)