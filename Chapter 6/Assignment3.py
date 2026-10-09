# Print all numbers between 1 and 50 except multiples of 5.

for num in range(1, 51, 1):
    if num % 5 == 0:
        continue
    print(num)