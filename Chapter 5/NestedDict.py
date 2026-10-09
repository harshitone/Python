# You can store another dictionary inside a dictionary.

studentProfile = {"Name": "Harshit Singh",
                  "Age": 31,
                  "Gender": "M",
                  "Address": {
                      "city": "Sirsaganj",
                      "State": "Uttar Pradesh",
                      "PIN": 283151
                  }
                  }
print(studentProfile["Name"])
print(studentProfile["Address"]["city"])