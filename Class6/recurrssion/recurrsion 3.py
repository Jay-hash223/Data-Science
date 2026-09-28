# sum of numbers using recurssion

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

print(sum_of_numbers(5))  # Output: 15

