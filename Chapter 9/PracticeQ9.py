# Create class FoodOrder with item name, quantity, price. Add method to calculate bill.

class FoodOrder:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def calculate_Bill(self):
        total = self.quantity * self.price
        print(f"Item Is {self.item_name} quantity is {self.quantity} & Total Amount is {total} ")

f1 =FoodOrder("pizza", 3, 360)
f1.calculate_Bill()


