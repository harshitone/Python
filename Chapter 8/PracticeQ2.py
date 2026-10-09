# Write a program to read a text from a given file certificate.txt and find 
# whether it contains the word live. 

with open("certificate.txt", "r") as file:
    data = file.read()
    print(data)

if "live" in data:
    print("Live is in the certificate.txt")
else:
    print("Live is not in certificate.txt")