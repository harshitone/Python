# User input

name = input("What is your name: ")
print("Hello!", name.title().strip())

greet = input("How are you: ")
print(greet.title())

age = int(input("How old are you: "))
print(age)
print("So Nice to talk to you Mr.",name.split()[0].title())
