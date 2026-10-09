# Read a file named story.txt and print the full content.

with open("story.txt", "r") as file:
    data = file.read()
    print(data)