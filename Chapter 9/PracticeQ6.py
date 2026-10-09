# Task: 
#  Create an Account class with: 
# ● Attributes → balance, account number 
 
# ● Methods → debit, credit, print balance


class Account:
    def __init__(self, balance, accountNumber):
        self.balance = balance
        self.accountNumber = accountNumber


   
    def credit(self, amount):
        self.balance += amount
        print("Amount Credited:", amount)

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Debit is :", amount)
        else:
            print("Insufficient Fund")

    def showBal(self):
        print("Account:", self.accountNumber , "Balance:", self.balance)

a1 = Account(50000, "H12345")
a1.credit(4500)
a1.debit(2700)
a1.showBal()

