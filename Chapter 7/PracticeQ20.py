# Write a function that returns both the sum and average of 5 inputs.

def check_sum_avg(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    avg = (num1 + num2 + num3 + num4 + num5) / 5
    return sum, avg

Sumresult, avgResult = check_sum_avg(2,4,6,8,9)
print("Sum of 5 numbers are:", Sumresult)
print("Average of 5 numbers are:", avgResult)