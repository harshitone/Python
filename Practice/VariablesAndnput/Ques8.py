# Take a number from the user and print its multiplication table from 1 to 10.

num = int(input("Please enter the number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")