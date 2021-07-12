class User:
    # Attributes
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.age = 24


    # Methods
    def make_deposit(self, deposit):
        self.account_balance += deposit
        return self


    def make_withdrawal(self, withdraw):
        if self.account_balance >= withdraw:
            self.account_balance -= withdraw
        return self


    def display_user_balance(self):
        print(f"{self.name} has ${self.account_balance}.")
        return self


    def transfer_money(self, other_user, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            other_user.account_balance += amount
        else:
            print("Not enough funds.")
        return self


guido = User("Guido", "guido@dojo.com") # this is 1 instance of User
# print(guido.name)


samer = User("Samer", "syahia@dojo.com") # this is another instance of User
samer.make_deposit(10000)
# print(samer.account_balance)
# print(guido.account_balance)

guido.make_deposit(50000).make_withdrawal(50).make_deposit(25).make_withdrawal(1250).transfer_money(samer, 5000).display_user_balance()
