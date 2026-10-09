# Write a program to print the multiplication table of any number using a while loop. 

num = int(input("Please enter the number: "))
count = 1

while count <= 10:
    print(f"{num} * {count} = {num * count}")

    count = count + 1