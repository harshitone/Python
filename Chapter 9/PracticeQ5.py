# Create static method to validate if a number is even.

class student:
    @staticmethod
    def checkEven():
        usrInput = int(input("Enter the Number: "))
        if usrInput % 2 == 0:
            print("Number is Even")
        else:
            print("Number is not Even")

s1= student()
s1.checkEven()
#student.checkEven()