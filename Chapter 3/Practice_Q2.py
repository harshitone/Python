# Write a python program that take your favorite place as user input and print
# middle 3 char
# last 3 char
# start 4 char

str = input("Enter your Favorite Place: ")
midChar = len(str)//2
print("Middle 3 char are:", str[midChar-1:midChar+2])
print("Last 3 char are:", str[-3:])
print("Starting 4 char are:", str[0:4])