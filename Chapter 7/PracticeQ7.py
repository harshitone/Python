# Create a function add_numbers(a, b) that prints both the sum and difference. 

def add_numbers(a=10, b=20):
    sum = a + b
    diff = a - b
    return sum, diff
sumResult, diffResult = add_numbers(5, 2)
print(f"Sum of two numbers are: {sumResult} \nDifference of two numbers are: {diffResult}")