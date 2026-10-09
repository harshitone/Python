# Goal: 
# Print a countdown before something “exciting” happens (like “Launching…” or 
# “Happy New Year!”).

import time as t

count = int(input("Please Enter the countDown Timer: "))
print("\nCountDown starts now!")
for num in range(count, 0, -1):
    print(num)
    t.sleep(1)
print(" !!Happy New Year!! ")