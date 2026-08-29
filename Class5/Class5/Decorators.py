# Decorators:

def decorator_function(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper


@decorator_function
def greet():
    print("Bharat")


greet()


# Using the decorator without the @ syntax.

def another_greet():
    print("Namaste")


another_greet = decorator_function(another_greet)
another_greet()


# More examples of decorators.
def uppercase_decorator(func):
    def wrapper(message):
        original_result = func(message)
        return original_result.upper()
    return wrapper


@uppercase_decorator
def greet(message):
    return message


print(greet("Vanakam!"))

# Adding more examples of decorators:

import time
from functools import wraps


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function():
    time.sleep(5)
    return "Completed"
print(slow_function())


# Decorator with arguments
def repeat_decorator(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat_decorator(5)
def say_hello():
    print("Hello")


say_hello()


# Decorator for logging:
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


print(add(3, 4))



