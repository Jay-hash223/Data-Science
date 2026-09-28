try:
    print(10 / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    
except TypeError:
    print("Error: Incompatible types for division.")

def add():
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        result = x + y
        return result
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    