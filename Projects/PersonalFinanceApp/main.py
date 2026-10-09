# Expense Tracker Project

expensesList = []

while True:
    print("\nWelcome to Expense Tracer 💸\n")
    print("======= MENU =======")
    print("1️⃣  Add Expense")
    print("2️⃣  View All Expenses")
    print("3️⃣  View Total Spending")
    print("4️⃣  Exit")

    choice = int(input("Please Enter Your Choice (1-4): "))

# ADD EXPENSES

    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter Category like (shopping/Food/Travel): ")
        desc = input("Add Short Discription: ")
        amount = float(input("Total Amount: "))

        expense = {"date": date, 
                   "category": category, 
                   "desc": desc, 
                   "amount": amount
        }

        expensesList.append(expense)
        print("\n!!Expenses Added Successfully!!\n")

# VIEW EXPENSES

    elif choice == 2:
        if len(expensesList) == 0:
            print("\n!!No Expenses Added Yet!!\n")
        else:
            print("======= List =======\n")
            count = 1
            for items in expensesList:
                print(f"{count}- {items["date"]}, {items["category"]}, {items["desc"]}, {items["amount"]} ")
                count +=1

# VIEW TOTAL SPENDING

    elif choice == 3:
        total = 0
        for item in expensesList:
            total = total + item["amount"]
        print("\n =============Your Total Expenses ============\n", total )

# Exit

    elif choice == 4:
        print("Thank You")
        break


    else:
        print("Invalid Choice")



