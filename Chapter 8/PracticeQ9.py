# Print how many lines are present in story.txt. 

with open("story.txt", "r") as file:
    data = len(file.readlines())
    #length = len(data)
    print(data)