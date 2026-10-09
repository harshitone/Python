# Bill Split Calculator
#Write a program that takes total bill amount and number of friends as input. 
#Calculate how much each person will pay. 
#Also print the data type of each variable used. 

friends = int(input("Enter total number of friends: "))
print("Total number of friends are:", friends)
print(type(friends))

totalAmount = int(input("Enter total Amount: "))
print("Total bill amount is ₹",totalAmount)
print(type(totalAmount))

billPaid = float(totalAmount / friends)
print("Amount will paid each friend is ₹",billPaid)
print(type(billPaid))