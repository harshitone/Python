# Read only the first line of story.txt.

with open("story.txt" ,"r") as file:
    data = file.readline()
    print(data)