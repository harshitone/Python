# Append "Completed" to an existing file status.txt.

with open("status.txt" , "a") as file:
    data = file.write("Name: Harshit Singh\n")
    data = file.write("class: Python programming\n")
    data = file.write("Learn Python Programming\n")
    data = file.write("Learn NumPy\n")
    data = file.write("Learn Panda")