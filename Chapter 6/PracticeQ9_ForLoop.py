#  Write a program to print numbers from 1 to 50, but print "Harshit Singh" instead of numbers
#  that are multiples of 5.

for num in range(1, 51, 1):
    if num % 5 == 0:
        print("Harshit Singh")
    else:
        print(num)