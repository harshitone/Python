# Create class Student with name, class, marks. Add method get_percentage().

class student:
    totalMarks = 500

    def __init__(self, Name, Class, Marks):
        self.Name = Name
        self.Class = Class
        self.Marks = Marks

    def get_percentage(self):
        self.Marks = (self.Marks/500)* 100
        print(f"Student name: {self.Name}\nclass: {self.Class}\npercentage: {self.Marks}%.")

s1= student("Harshit", 12, 480)
s1.get_percentage()

