# Lambda Function
xyz = lambda x: x * 2
print(xyz(5))  # Output: 10

# Lambda function with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7


# lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!


# Lambda function with default arguments
multiply = lambda x, y=2: x * y
print(multiply(3))  # Output: 6
print(multiply(3, 4))  # Output: 12 

# Lambda function with variable-length arguments
sum_all = lambda *args: sum(args)   
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
# Lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  



# Lambda function with default argument
power = lambda x, y=2: x ** y
print(power(3))      # Uses default argument y=2, Output: 9
print(power(2, 3))   # Overrides default argument, Output: 8
# Lambda function with variable-length arguments
concat = lambda *args: ''.join(args)
print(concat("Hello", " ", "World"))  # Output: Hello World

def add(*args):
    return sum(args)

result = add(1,2,3) #output:6
print(result)
print(add(10, 20, 30,23,12  ))  # Output: 60