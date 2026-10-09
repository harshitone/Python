# A tuple is a built-in data type that stores multiple values like a list, but it is 
# immutable (cannot be changed after creation). 

Animals = ("Cow", "Tiger", "Lion", "Elephant", "Jaguar")
print(type(Animals))
print(Animals)

# Indexing

print(Animals[4])
print(Animals.index("Tiger"))

# Slicing

print(Animals[0:2])
print(Animals[:3])
print(Animals[-3:])
print(Animals[-4:-1])

# Empty Tuple
food = ()
print(food)
print(type(food))

num = (1,) # use , after single element for tuple class, otherwish it shows int class
print(num)
print(type(num))

# Note: we can not modify elements in tuple once created.