# List creation

sports = ["Cricket", "Badminton", "Tennis", "Ludo", "WWE", "Table Tennis", "PlayStation"]
print(sports)
print(type(sports)) # list

# List Indexing

print(sports[4]) # WWE
print(sports[0]) 
print(sports[5]) 
print(sports[2]) 
print(sports.index("Badminton")) # 1 index 
print(sports.index("Cricket"))
print(sports.index("Ludo"))
print(sports.index("PlayStation"))

# List Slicing

print(sports[0:4]) #['Cricket', 'Badminton', 'Tennis', 'Ludo']
print(sports[-3:]) # ['WWE', 'Table Tennis', 'PlayStation']
print(len(sports)) # 7

# List are changable/ Modify
print("Original List", sports)
sports[0] = "football" # change list at index 0
print("Updated list" ,sports)

# Methods in List
marks = [23, 34, 45, 78, 90]
marks.sort() # sorting the list
print(marks)
marks.append(10) # add element at last
print(marks)
marks.remove(10) # remove element from list
print(marks) 
marks.pop(1) # remove element from index 1
print(marks)
marks.insert(1,40) # insert element at index 1 and value is 40
print(marks)
marks.reverse() # reverse elements in list
print(marks)


# Functions in List

print(max(marks))
print(min(marks))
print(len(marks))