# Mini Project – Guess the Number Game 
# Concepts Used: while loop and user input.

import random

secret_num = random.randint(1,10)
print(secret_num)

usrInput = int(input("Please guess the number between 1 to 10: "))
n = 1
while n <= 3:
    if usrInput == secret_num:
        print("Congratulation!🎉 You have guessed the correct number 🏆")
        break
    else:
        print("Sorry You have guessed the wrong number\n")
        if n < 3:
            print("Please Try Again!\n")
            usrInput = int(input("Please guess the number between 1 to 10: "))
    n = n + 1
if usrInput != secret_num:
    print("Sorry! You have reached the maximum number of attempts.\n")
    print(f"The correct number was {secret_num}.")
       
    # if usrInput != secret_num:
    #     print("Sorry You have guessed the wrong number\n")
    #     print("Please Try Again!\n")
    #     usrInput = int(input("Please guess the number between 1 to 10: "))
    #     n = n + 1
    
    # print("Sorry You have Reached the Maximum Number Of limit!")
