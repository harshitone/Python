# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects with different values.

class Laptop:
    #brand = input("Please enter the Brand Name: ")
    brand = "Dell"
    ram = "16GB"
    price = "₹45000"

    # def __init__(self, brand):
    #     self.brand = brand
        

#L1 = Laptop("Macbook")
L1 = Laptop()
L1.brand= "Macbook"
print(L1.brand)
#L1.brand= "Macbook"
#L1.model= 2026
#print(L1.model)

L2 = Laptop()
L2.brand= "HP"
print(L2.brand)