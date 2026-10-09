# Write a function to print even numbers from 2 to N. 

def check_even(num):
    for i in range(2, num, 2):
        if i % 2 == 0:
            print(i)
check_even(20)