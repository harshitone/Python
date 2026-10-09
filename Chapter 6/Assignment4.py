# Create a program that asks the user for 5 favorite foods and prints them one by one.

foodList = []

for favfood in range(5):
    item = input("Please enter your five favourite foods: \n")
    foodList.append(item)
print(f"Harshit likes {foodList}.")