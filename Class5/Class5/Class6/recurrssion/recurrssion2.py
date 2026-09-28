# Fibonacci sequence usinf recurrsion

def fibonacci(n):
        if n <= 2:
            
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))  




# Example of recurrsion with string reveral

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH