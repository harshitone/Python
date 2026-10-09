# Create class Creator with attributes (name, username). Add method bio().

class Creator:
    def __init__(self,name,username):
        self.name= name
        self.username= username

    def bio(self):
        print(f"Name is {self.name} & username is {self.username}")

c1 = Creator("Harshit", "Harshitone")
c1.bio()