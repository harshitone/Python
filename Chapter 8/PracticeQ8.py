# Print all the lines in story.txt

with open("story.txt", "r") as file:
    data = file.readlines()
    print(data)