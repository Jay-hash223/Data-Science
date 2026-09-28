# Anonymous Functions:

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8


# adding more examples of lambda function:

#Examles with map:

squared = list(map(lambda x: x**2,range(6)))
print(squared)  # Output: [0, 1, 4, 9, 16, 25]

# Examples with filter:

even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(even_numbers)  # Output: [0, 2, 4,

# Examples with reduce:
from functools import reduce
product = reduce(lambda x, y: x * y, range(1, 6))
print(product)  # Output: 120

# Examples with sorting:
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, 0), (3, 1), (1, 2)]
# Example with default arguments:
greet = lambda name="World": f"Hello, {name}!"
print(greet())  # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!
def make_incrementer(n):
    return lambda x: x + n

increment_by_5 = make_incrementer(5)
print(increment_by_5(10))  # Output: 15
print(increment_by_5(20))  # Output: 25
increment_by_10 = make_incrementer(10)
print(increment_by_10(10))  # Output: 20    
print(increment_by_10(20))  # Output: 30
# Example with multiple arguments
def apply_operation(x, y, operation):
    return operation(x, y)  
result = apply_operation(10, 5, lambda a, b: a - b)
print(result)  # Output: 5
result = apply_operation(10, 5, lambda a, b: a * b)
print(result)  # Output: 50 
result = apply_operation(10, 5, lambda a, b: a / b)
print(result)  # Output: 2.0    
# Example with sorting complex structures
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 23}
]
students.sort(key=lambda student: student['age'])
print(students)
# Example with nested lambda functions
nested_lambda = lambda x: (lambda y: x + y)
print(nested_lambda(5)(10))  # Output: 15
# Example with conditional expressions
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))  # Output: 20
print(max_value(30, 15))  # Output: 30
# Example with list comprehensions and lambda
incremented_list = [(lambda x: x + 1)(x) for x in range(5)]
print(incremented_list)  # Output: [1, 2, 3, 4, 5]
# Example with sorting based on multiple criteria
data = [(1, 'apple'), (2, 'banana'), (1, 'orange'), (2, 'grape')]
data.sort(key=lambda item: (item[0], item[1]))
print(data)  # Output: [(1, 'apple'), (1, 'orange'), (2, 'banana'), (2, 'grape')]