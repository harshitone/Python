# Write a program that takes names of 3 favorite foods from the user and stores 
# them in a list. Then print the list and its length.

food1 = input("Enter the First Favorite Food: ")
food2 = input("Enter the Second Favorite Food: ")
food3 = input("Enter the Third Favorite Food: ")

storeFood = [food1, food2, food3]
print(storeFood)
print("Total Items:", len(storeFood))