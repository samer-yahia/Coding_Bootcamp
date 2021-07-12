class BankAccount:
# Attributes
    bank_instances = []
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.bank_instances.append(self)


#Methods
    #Method will add the amount given to balance
    def deposit(self, amount):
        self.balance += amount
        return self

    #If enough funds, subtracts an amount from balance. If not $5 fee
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    # Displays the available amount in balance
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    #Will calculate and display total of balance after interest yield
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


    @classmethod
    def print_all_instance(cls):
        print("All Instances of Bank Account")
        for amount in cls.bank_instances:
            amount.display_account_info()


class User:
# Attributes
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0, 0.02)


# Methods
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self


    def display_account_info(self):
        self.account.display_account_info()
        return self


# Make the user then use chain method to deposit, withdraw, and display account info
samer = User("Samer", "syahia@dojo.com")

samer.make_deposit(10000).make_withdraw(5000).display_account_info()
