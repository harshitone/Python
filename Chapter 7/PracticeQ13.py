# Define a function message(text="Keep Learning!") and call it with and without an argument. 

def message(text="Keep Learning!"):
    return text

# Method1 print through store data in variable and print variable
withoutArgu = message()
print(withoutArgu)
withArgu = message("Keep Learning!")
print(withArgu)

# Method2 print direct funaction call with and without arguments.
print(message())
print(message("Keep Learning!"))