#  Create a class FoodItem with class attribute category = "Snacks" and instance 
# attribute name (“Samosa”, “GulabJamun”). 

class FoodItem:
    category = "Snacks"
    def __init__(self, name):
        self.name = name

item1 = FoodItem("Samosa")
item2 = FoodItem("GulabJamun")
print(item1.name)
print(item2.name)
print(item1.category)