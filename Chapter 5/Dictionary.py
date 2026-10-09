# A dictionary is a built-in data type in Python used to store data in key–value 
# pairs. 
# Each key is unique and maps to a value. 
# Dictionaries are unordered, mutable (changeable), and don’t allow duplicate keys. 

student = {"name": "Harshit Singh",
           "age": 31,
           "Gen": "M",
           "City": "Agra",
           "Profession": "Engineer"
           }
print(type(student))
print(student["name"])
print(student)

# Adding/Modify value
student["collage"] = "PSIT"
print(student)

# Methods in dictionary

print(student.keys()) # Return Keys
print(student.values()) # Return values
print(student.items()) # Return both keys and values
print(student.get("name")) 
print(student["name"])
student.update({"name": "Harshit Jadon"})
print(student)