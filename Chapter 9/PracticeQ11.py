# Bank Account (Final Project) 
# Add debit/credit logs and private balance. 


class BankAccount():    
    def __init__(self, accountNum, initial_bal):
        self.accountNum = accountNum
        self.initial_bal = initial_bal
        self.logs = []

    def credit(self, amount):
        if amount<=0 :
            print("Insufficiant Fund")
            return

        self.initial_bal += amount
        self.logs.append(f"Credited: {amount}. Balance: {self.initial_bal}")
        print(f"You have credited {amount} \nCurrentBalance {self.initial_bal}")

    def debit(self, amount):
        if amount <= 0 :
            print("Insufficient Balance")
        elif amount > self.initial_bal :
            print("Insufficeint Balance")

        else:
            self.initial_bal -= amount
            self.logs.append(f"Debited: {amount}. Balance {self.initial_bal}")
            print(f"Debited Amount {amount} \nCurrentBalance {self.initial_bal}")

    
    def show_logs(self):
        print(" --- Transaction History --- ")
        for eachEntry in self.logs:
            print(eachEntry)

A1 = BankAccount(3456786, 60000)
A1.credit(4000)
A1.debit(20000)
A1.show_logs()


   