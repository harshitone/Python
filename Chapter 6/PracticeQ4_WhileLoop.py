# Write a program that prints the sum of first n natural numbers. 
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.

num = int(input("Please enter the number: "))
sum = 0


while num >= 1:
    sum = sum + num
    num = num - 1

print(sum)
