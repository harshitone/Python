#Write a program that takes two numbers and prints: 
#● Their sum, difference, and product 
#● Whether the first number is greater than the second

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
find = bool(num1 > num2)
print("Sum of the number is:", sum)
print("Difference of the number is:", diff)
print("Multiplication of the number is:", prod)
print("Is num1 is greater than num2 ?",find)