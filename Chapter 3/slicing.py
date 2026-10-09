# Understanding slicing concept

str = "Kedarnath"

# K E D A R N A T H
# 0 1 2 3 4 5 6 7 8
#-9-8-7-6-5-4-3-2-1

# Syntax str[start:end]

print(str[0:5]) # Return Kedar
print(str[:5]) # Return Kedar, by default it, will start from start index.
print(str[5:9]) # return nath
print(str[5:]) # return nath, by default it, will go to end index.
print(str[-5:]) # return rnath
print(str[:-4]) # kedar