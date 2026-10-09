# Append the current date and time to a file logs.txt whenever the program runs.

import datetime


with open("logs.txt", "a") as logFile:
    data = logFile.write(f"Harshit logged in at {datetime.datetime.now()}")