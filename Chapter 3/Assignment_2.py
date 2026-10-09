# write a program that takes any sentance or word as a input
# print first charcter
# print last 2 charcter
# print total number of charcter

Sent = input("Enter the sentance/word: ")
print("First charcter is:", Sent[0])
print("Last two charcter is:", Sent[-2:])
Senlength = Sent.replace(" ","")
print("Total number of charcter is:", len(Senlength))
wordCount = len(Sent.split())
print("Total words are:", wordCount)