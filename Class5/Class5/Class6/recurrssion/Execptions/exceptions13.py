try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")   
finally:
    print("Execution completed")
        