# You are given a list of programming languages: 
# ["Python", "Java", "C++", "Python", "Java", "C"] 
# Convert it into a set and print how many unique languages Harshit knows.

List = ["Python", "Java", "C++", "Python", "Java", "C"]
List = set(List) # Type casting
print(List)
print(type(List))
print("Harshit knows", len(List), "Unique languages.")