statement = "Python is easy"
print(statement)
print(statement[0])
print(statement[-1])


# Example:
#Example code to demonstrate reading in python 3.x

#raw input code
# 
value = int(input("Please enter  an integer"))
print("you entered",value)

# raw input code

p = bool_value = bool(input("Please enter a string:"))
print("You enterd:,bool_value")

#raw input code

string_value = str(input("Please enter a string: "))
print("You entered:", string_value)
#raw input code
float_value = float(input("Please enter a floating-point number: "))
print("You entered:", float_value)

#Observe the behaviour of different data types with raw input in python 2.x and input in python 3.x
# In python 2.x input() reads input as a string, When you enter the values like 10,10.5,True,"Hello" in the input prompt.
# Note: In Python 2.x, raw input as python expression.


# Changing cases:
# Example:
statement= "Rishi Kumar"
print(statement.upper())   # RISHI KUMAR
print(statement.lower())   # rishi kumar
print(statement.title())   # Rishi Kumar
print(statement.swapcase())# rISHI kUMAR

import math
print(math.ceil(4.2))  # 5
print(math.floor(4.7)) # 4

print(  math.sqrt(16))  # 4.0
print(  math.factorial(5)) # 120

# CHeck type characthers:

name = "India"

print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.ispace())

# String Concepts

s = "Python_Sampath"
print("Sampath" not in s)     # True
print("abc"  in s) 

# Checking Start and End
str = "Hello World"
print(str.startswith("Hello")) 
print(str.endswith("World"))  

# Comparision of strings:

fruit1 = "apple"
fruit2 = "banana"
print(fruit1 == fruit2)   # False
print(fruit1 < fruit2)

# Couting Substring:

s = "banana"
print(s.count("a))"))

# Finding_substring:

s = "python programming"
print(s.find("gramm"))
print(s.find("xyz"))

# Reverse a string

s = "python"
print(s[::])

#Palindrome check:

word = "madam"
print(word==word[::1])

#count cowels

s = "Hello World"
vowels = "aeiouAEIOU"

count = sum(1 for char in s if char in vowels)
print(count)

# Joining String

fruits = ["apple","banana","cherry"]
print(",".joint(fruits))

# Length of funtion:

s = "Python"
print(len(s))

# Mathamatical Operators:

a = "Hello"
b = "World"
print(a + " " + b)  
print(a * 3)  

# Multiline string:

multi_line = """this is a multi-line string"""
print(multi_line)

#removing space:
s = "  Hello World  "
print(s.strip())      
print(s.lstrip())       
print(s.rstrip()) 

# Replacing String:

s = "I like Java"
print(s.replace("Java", "Python"))

# Slice Operator:

s = "Python"
print(s[1:4])  
print(s[:2])   
print(s[2:])   

# Slice operators

s = "Programming"
print(s[3:8])    # rammi
print(s[::-1])

# Slipt Strings:
s = "apple,banana,cherry"
print(s.split(","))

# String data type:

s = "Hello, World!"
print(type(s))

# Whats the string:

s = "Python is fun"
print(s)

