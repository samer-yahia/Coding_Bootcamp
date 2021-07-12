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

guido = User("Guido", "guido@dojo.com") # this is 1 instance of User
# print(guido.name)

guido.make_deposit(5000)
# print(guido.account_balance)

samer = User("Samer", "syahia@dojo.com") # this is another instance of User
samer.make_deposit(10000)
print(samer.account_balance)
print(guido.account_balance)

# guido.name = "Guido"
# print(guido.name)



# class User:
#     # declaring a class attribute
#     bank_name = "First National Dojo"		
#     def __init__(self): # constructor
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()
# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union 
# print(monty.bank_name) # output: First National Dojo