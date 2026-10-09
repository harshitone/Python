# Count how many words are present in the file story.txt

with open("story.txt" ,"r") as file:
    data = file.read()
    word_count = len(data.split())
    print(word_count)
