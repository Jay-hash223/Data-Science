# ===== BASIC DICTIONARIES WITH LIST VALUES =====
print("=" * 60)
print("EXAMPLE 1: Basic Dictionaries with List Values")
print("=" * 60)

d = {'fruits': ['apple', 'banana']}
d2 = {'marks': [85, 90, 95]}
d3 = {'letters': list('abc')}
d4 = {'nums': list(range(5))}
d5 = {'data': [1.1, 2.2, 3.3]}

print("d:", d)
print("d2:", d2)
print("d3:", d3)
print("d4:", d4)
print("d5:", d5)

# ===== ACCESSING ELEMENTS FROM LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 2: Accessing Elements from List Values")
print("=" * 60)

print("First fruit:", d['fruits'][0])
print("Second fruit:", d['fruits'][1])
print("All marks:", d2['marks'])
print("First mark:", d2['marks'][0])
print("Last letter:", d3['letters'][-1])
print("All numbers:", d4['nums'])

# ===== APPENDING AND EXTENDING LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 3: Appending and Extending List Values")
print("=" * 60)

print("Before append - d:", d)
d['fruits'].append('orange')
print("After append - d:", d)

d['fruits'].extend(['grape', 'mango'])
print("After extend - d:", d)

d2['marks'].append(88)
print("After appending mark - d2:", d2)

# ===== REMOVING ELEMENTS FROM LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 4: Removing Elements from List Values")
print("=" * 60)

d_test = {'colors': ['red', 'green', 'blue', 'yellow']}
print("Original d_test:", d_test)
d_test['colors'].remove('green')
print("After remove('green'):", d_test)
print("After pop():", d_test['colors'].pop())
print("After pop(0):", d_test['colors'].pop(0))
print("Final d_test:", d_test)

# ===== ITERATING THROUGH LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 5: Iterating Through Dictionary with List Values")
print("=" * 60)

student_marks = {'Alice': [90, 85, 92], 'Bob': [78, 88, 95], 'Charlie': [88, 91, 85]}
print("Student marks:", student_marks)

for student, marks in student_marks.items():
    print(f"\n{student}'s marks: {marks}")
    for i, mark in enumerate(marks, 1):
        print(f"  Subject {i}: {mark}")

# ===== SORTING LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 6: Sorting List Values")
print("=" * 60)

scores = {'math': [45, 78, 23, 95, 67], 'english': [88, 92, 76, 85, 91]}
print("Original scores:", scores)

sorted_scores = {key: sorted(value) for key, value in scores.items()}
print("Sorted scores:", sorted_scores)

sorted_desc = {key: sorted(value, reverse=True) for key, value in scores.items()}
print("Sorted (descending):", sorted_desc)

# ===== CALCULATING STATISTICS ON LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 7: Calculating Statistics from List Values")
print("=" * 60)

data = {'scores': [85, 90, 78, 92, 88, 95]}
print("Data:", data)
print("Sum:", sum(data['scores']))
print("Average:", sum(data['scores']) / len(data['scores']))
print("Max:", max(data['scores']))
print("Min:", min(data['scores']))
print("Count:", len(data['scores']))

# ===== FILTERING LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 8: Filtering List Values")
print("=" * 60)

numbers = {'values': [12, 45, 23, 67, 34, 89, 56, 12, 90, 11]}
print("Original numbers:", numbers)

even_numbers = [x for x in numbers['values'] if x % 2 == 0]
print("Even numbers:", even_numbers)

numbers_above_50 = [x for x in numbers['values'] if x > 50]
print("Numbers above 50:", numbers_above_50)

# ===== MODIFYING LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 9: Modifying List Values")
print("=" * 60)

prices = {'items': [10, 20, 30, 40, 50]}
print("Original prices:", prices)

prices['items'] = [x * 1.1 for x in prices['items']]
print("After 10% increase:", prices['items'])

# Change specific element
prices['items'][0] = 15
print("After changing first price:", prices)

# ===== COMBINING MULTIPLE LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 10: Combining Multiple List Values")
print("=" * 60)

d_combine = {'list1': [1, 2, 3], 'list2': [4, 5, 6], 'list3': [7, 8, 9]}
print("Original:", d_combine)

combined = []
for key, value_list in d_combine.items():
    combined.extend(value_list)
print("Combined list:", combined)

# Combine into new dictionary
combined_dict = {'all_values': combined}
print("Combined dictionary:", combined_dict)

# ===== NESTED DICTIONARIES WITH LISTS =====
print("\n" + "=" * 60)
print("EXAMPLE 11: Nested Dictionaries with Lists")
print("=" * 60)

company = {
    'dept1': {'employees': ['John', 'Jane'], 'budget': [1000, 2000]},
    'dept2': {'employees': ['Bob', 'Alice'], 'budget': [1500, 2500]}
}
print("Company data:", company)

for dept, info in company.items():
    print(f"\n{dept}:")
    print(f"  Employees: {info['employees']}")
    print(f"  Budget: {info['budget']}")

# ===== FINDING ELEMENTS IN LIST VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 12: Finding Elements in List Values")
print("=" * 60)

inventory = {'books': ['Python', 'Java', 'C++', 'JavaScript', 'Python']}
print("Inventory:", inventory)

if 'Python' in inventory['books']:
    print("Python book found!")
    print("Position:", inventory['books'].index('Python'))
    print("Count:", inventory['books'].count('Python'))

# ===== CREATING DICTIONARY FROM LIST =====
print("\n" + "=" * 60)
print("EXAMPLE 13: Creating Dictionary from List Values")
print("=" * 60)

data_list = ['apple', 'banana', 'cherry', 'date']
d_from_list = {item: [ord(c) for c in item] for item in data_list}
print("Dictionary with character codes:", d_from_list)