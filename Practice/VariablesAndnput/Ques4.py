# Take an integer from the user and determine whether it is even or odd.

usrinput = int(input("Enter the number: "))

while True:
    if usrinput % 2 == 0:
        print("Number is Even")
        break
    
    else:
        print("Number is odd")
        break