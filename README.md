# Data-Science
Data Science
# i made some changees

# made changes
# cloned sucessfully!
x = "10"
y = 3
result = x + str(y)
print(result)  # Output: "103"

str = "User.Name@Domain.Com"
print(str.lower())

user_ids = [101,102,101,103,102]
set(user_ids)
print(set(user_ids))

course_data = {
    "class": "Class4",
    "details": {
        "subject": "Python",
        "level": 1
    }
}
print(course_data)  

user_input = "My_User_Name_123"
print(user_input.lower())

user_message = "Hey checkout this AWESOME deal to win FREE money now!!"

# 1. Convert the whole message to lowercase, then check for "free"
if "free" in user_message.lower():
    print("Spam message detected")
else:    
    print("Message Approved")


# The list of words you want to block
blacklist = ["free", "winner", "crypto", "bonus"]


user_message = "Congratulations! You are the lucky winner of today's raffle!"

# Check if any blacklisted word is in the message
is_spam = False
for word in blacklist:
    if word in user_message.lower():
        is_spam = True
        break

if is_spam:
    print("Spam message detected")
else: 
    print("Message Approved")


import math

height = 14.7          # in meters
wind_speed = 22        # in km/h
pad_is_clear = True    # True means no obstacles, False means blocked

# 1. Round down the height using the math module
rounded_height = math.floor(height)

print("Height of the tower:", rounded_height, "meters")
print("Wind speed:", wind_speed, "km/h")

# 2. Check all three conditions together
if rounded_height < 15 and wind_speed < 25 and pad_is_clear:
    print("Initiating landing sequence...")
else:
    print("Landing aborted! Hold position.")

fset = frozenset("vowels")
print("The frozen set is:", fset)
print("The empty frozen set is:", frozenset())

# 1. Take input and convert the string into an integer
age_input = input("Enter your age: ")
age = int(age_input)

# 2. Check the brackets using relational operators
if age < 12:
    print("Ticket price: ₹100 (Child Discount)")
elif age >= 65:
    print("Ticket price: ₹150 (Senior Discount)")
else:
    print("Ticket price: ₹250 (Standard Rate)")






# A list of user inputs to check
raw_inputs = ["  ACCESS ", " denied ", "  AcCeSs  ", " error ", "  access   "]

# Variable to count how many inputs successfully match the word "access"
success_count = 0

for input_str in raw_inputs:
    if input_str.strip().lower() == "access":
        success_count += 1

print("Number of successful matches:", success_count)



students_data = {
    "student_1": {
        "name": "Amit",
        "scores": {"Math": 85, "Science": 90}
    },
    "student_2": {
        "name": "Rahul",
        "scores": {"Math": 55, "Science": 65}
    }
}
dict = students_data["student_1"]["scores"]
students_data["student_2"]["scores"]["Math"] = 75

print("Student 1 Name:", students_data["student_1"]["name"])
print("Student 1 Math Score:", students_data["student_1"]["scores"]["Math"])
print("Student 1 Science Score:", students_data["student_1"]["scores"]["Science"])
print("Student 2 Math Score:", students_data["student_2"]["scores"]["Math"])
print("Student 2 Science Score:", students_data["student_2"]["scores"]["Science"])



server_A = {101, 102, 103, 104}
server_B = {103, 104, 105, 106}
print(set(server_A).union(set(server_B)))


list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)

print("list_a:", list_a)
print("list_b:", list_b)


for num in [1, 2, 3, 4, 5]:
    if num == 5:
        print("Found 5!")
        break
else:
    print("Number 5 was not in the list.")



squares = []
for x in range(1, 6):
    if x % 2 != 0:
        squares.append(x * x)

print("Squares of odd numbers from 1 to 5:", squares)



squares = [x * x for x in range(1, 6) if x % 2 != 0]

print("Squares of odd numbers from 1 to 5:", squares)
