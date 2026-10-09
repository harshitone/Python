# Write code to open a file named mydata.txt in read mode.

with open("mydata.txt", "r") as m:
    data = m.read()
    print(data)