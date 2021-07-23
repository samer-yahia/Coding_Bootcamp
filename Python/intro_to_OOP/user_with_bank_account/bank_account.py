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




# Create bank accounts for users
samer = BankAccount(0, .05)
rashad = BankAccount(0, .1)

#Make 3 deposits, 1 withdraw, then show the total balance after interest yield
samer.deposit(5000).deposit(10000).deposit(1250).withdraw(1000).yield_interest()

# Make 2 deposits and 4 withdraws, then yield interst, and display the account's info
rashad.deposit(10000).withdraw(2000).withdraw(5000).deposit(3000).withdraw(1000).withdraw(2500).yield_interest().display_account_info()

# Ninja Bonus: Use a classmethod to print all instances of a Bank Account's Info

BankAccount.print_all_instance()
