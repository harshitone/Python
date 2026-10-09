# Write a program to safely check whether a file exists before opening it.

import os

fileName = "certificate.txt"
if os.path.exists(fileName):
    with open(fileName, "r") as file:
        print(file.read())
else:
    print("File does not Exist")