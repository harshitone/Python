# Ask user for diameter and length of square and then print the area of circle and area of square.

# print area of circle
diameter = int(input("Enter the diameter of Circle: "))
radius = diameter / 2
area = 3.14 * radius**2
print("Area of Circle is: ", area,"cm2")

# print area of square
length = int(input("Enter the length of one side of square: "))
#print(length)
areaSqaure = length**2
print("Area of Sq: ", areaSqaure,"cm2")