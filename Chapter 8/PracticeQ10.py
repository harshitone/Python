# Write your name and class into a file named intro.txt using with keyword

with open("intro.txt", "w") as file:
    line = file.write("Name: Harshit Singh\n")
    line = file.write("class: Python Programming")