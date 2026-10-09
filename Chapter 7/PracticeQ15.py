# Write a program with a local variable score inside a function and a global one outside.

score = 100 # Global Variable

def show_Score():
    score = 50 #Local Variable
    print("Inside Function variable Score", score)

print("Outside variable score", score)
show_Score()