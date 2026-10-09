# Create class Student that takes 3 marks and has a method average().

class student:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def average(self):
        sum = self.num1 + self.num2 + self.num3
        average = sum/3
        return ("average is", average)

s1 = student(95, 99, 100)
print(s1.average())

