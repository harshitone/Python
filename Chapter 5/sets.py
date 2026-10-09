# A set is a collection of unordered and unique items. Sets automatically remove duplicate elements and are written using curly braces { }.

progLanguages = {"Python", "Java", "C++", "C", "GoLang"}
print(progLanguages)

# Methods in sets

progLanguages.add("Assembly")  # add assembly language at last
progLanguages.remove("C++") # remove C++ language
print(progLanguages)

num1 = {1, 2, 4, 6, 7, 9}
num2 = {1, 3, 5, 8, 10}
print(num1.union(num2)) # both num1 & num2 join and print 1 in single time
print(num1.intersection(num2)) # print only 1
num1.pop()
print(num1)