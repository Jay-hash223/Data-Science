# Recursive Functions:
#Examples:

def square(y):
    if y == 1:
        return 1
    else:
        return y* square(y-1)
print(square(5))

# Function inside function:

def outer_function():
    print("i am outer function")
    def inner_function():
        print("i am inner function")
    inner_function()
    outer_function()

#inner function() # Error: name 'inner_function' is not defined.
#Example of recursion with inner function:
#more complex example of fuction inside funtion
#accesing variable of outer fintion inside inner function.
#factorial,fibonacci, sum of n numbers, sum of digits, power of number, reverse of number, palindrome, gcd, lcm, hcf, decimal to binary, binary to decimal, decimal to octal, octal to decimal, decimal to hexadecimal, hexadecimal to decimal, decimal to roman, roman to decimal, etc.
# Examples:

def outer_function():
    def inner_function(n):
        return inner_function(n-1) + n if n > 0 else 0
    return inner_function
result = outer_function()
print(result)


# #accesing variable of outer function inside inner function.

def fibnocci(n):
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    return fib(6)

#tail recursion example:
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n-1, n * accumulator)
print(tail_recursive_factorial(9))  # Output: 120        

# Function with default argument

def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!


#Function with variable-length arguments
def print_values(*args):
    for arg in args:
        print(arg)

print_values(1, 2, 3, 4, 5)

print_values("apple", "banana", "cherry")
print_values(3,4)
print("cherry")

# Function with keyword arguments
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(name="Alda", age=30)
print_info(age=25, name="Maark")

# Function with both variable-length and keyword arguments.

def print_details(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(1, 2, 3, name="Alda", age=30)
print_details("apple", "banana", fruit="cherry", color="red")
print_details(3,4, name="Alda", age=30, city="New York")
print_details("apple", "banana", fruit="cherry", color="red", country="USA")
print_details(1, 2, 3, name="Alda", age=30, city="New York", country="USA")
print_details("apple", "banana", fruit="cherry", color="red", country="USA", state="California")
print_details(1, 2, 3, name="Alda", age=30, city="New York", country="USA", state="California", zip_code="10001")
