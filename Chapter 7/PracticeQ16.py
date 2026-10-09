# Create a program using global keyword to modify a variable from inside a function. 

score = 50

def update_Score():
    global score
    score = 100
print("Before", score)

update_Score()
print("After", score)