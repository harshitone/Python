# Write a function that checks if a number is prime.

def check_prime(num):
    if num < 2:
        print("Not Prime")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return
    else:
        print("Prime Number")

    
check_prime(6)