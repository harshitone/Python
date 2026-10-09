# Add method to increase salary by a percentage

class Employee():
    def __init__(self, salary):
        self.salary =salary

    def increase_salary(self):
        increment = (self.salary * 20)/100
        print(f"Your current salary was {self.salary} and you have got increment by 20%. \nNow updated Salary is {self.salary + increment}")

E1 = Employee(15000)
E1.increase_salary()