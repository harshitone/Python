#  Write a program that prints the multiplication table of any number entered by 
# the user using a for loop.

num = int(input("Please enter the number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")