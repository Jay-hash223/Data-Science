# ===== BASIC DICTIONARIES WITH TUPLE VALUES =====
print("=" * 60)
print("EXAMPLE 1: Basic Dictionaries with Tuple Values")
print("=" * 60)

d = {'coords': (10, 20)}
d2 = {'rgb': (255, 255, 0)}
d3 = {'version': (3, 8)}
d4 = {'date': (2025, 7, 10)}
d5 = {'grades': ('A', 'B', 'C')}

print("d:", d)
print("d2:", d2)
print("d3:", d3)
print("d4:", d4)
print("d5:", d5)

# ===== ACCESSING ELEMENTS FROM TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 2: Accessing Elements from Tuple Values")
print("=" * 60)

print("X coordinate:", d['coords'][0])
print("Y coordinate:", d['coords'][1])
print("Red value:", d2['rgb'][0])
print("Green value:", d2['rgb'][1])
print("Blue value:", d2['rgb'][2])
print("Python version:", d3['version'])
print("Full date:", d4['date'])

# ===== TUPLE UNPACKING =====
print("\n" + "=" * 60)
print("EXAMPLE 3: Tuple Unpacking from Dictionary")
print("=" * 60)

x, y = d['coords']
print(f"Unpacked coordinates - X: {x}, Y: {y}")

r, g, b = d2['rgb']
print(f"Unpacked RGB - Red: {r}, Green: {g}, Blue: {b}")

year, month, day = d4['date']
print(f"Unpacked date - Year: {year}, Month: {month}, Day: {day}")

major, minor = d3['version']
print(f"Python version - Major: {major}, Minor: {minor}")

# ===== DICTIONARY WITH MULTIPLE TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 4: Dictionary Storing Different Tuple Information")
print("=" * 60)

points = {
    'point_a': (1, 2),
    'point_b': (3, 4),
    'point_c': (5, 6),
    'point_d': (7, 8)
}

print("Points dictionary:", points)
for point_name, coordinates in points.items():
    print(f"{point_name}: {coordinates}")

# ===== CALCULATING DISTANCE BETWEEN POINTS =====
print("\n" + "=" * 60)
print("EXAMPLE 5: Calculate Distance Between Coordinates")
print("=" * 60)

import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

dist = distance(points['point_a'], points['point_b'])
print(f"Distance between point_a and point_b: {dist:.2f}")

# ===== MODIFYING TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 6: Modifying Tuple Values (Creating New Tuples)")
print("=" * 60)

# Note: Tuples are immutable, so we create new ones
print("Original d:", d)
d['coords'] = (15, 25)  # Replace with new tuple
print("Modified d:", d)

# Add new tuple value
d['new_coords'] = (30, 40)
print("After adding new_coords:", d)

# ===== ITERATING THROUGH TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 7: Iterating Through Tuple Values")
print("=" * 60)

student_info = {
    'Alice': ('95', 'A', 'Science'),
    'Bob': ('87', 'B', 'Math'),
    'Charlie': ('92', 'A', 'English'),
    'Diana': ('78', 'C', 'History')
}

print("Student information:")
for name, info in student_info.items():
    score, grade, subject = info
    print(f"{name}: Score={score}, Grade={grade}, Subject={subject}")

# ===== SORTING BASED ON TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 8: Sorting Based on Tuple Values")
print("=" * 60)

employees = {
    'emp1': (2500, 'John'),
    'emp2': (3500, 'Alice'),
    'emp3': (2000, 'Bob'),
    'emp4': (4000, 'Charlie')
}

print("Original employees:", employees)

# Sort by salary (first element of tuple)
sorted_by_salary = sorted(employees.items(), key=lambda x: x[1][0])
print("\nSorted by salary:")
for emp_id, (salary, name) in sorted_by_salary:
    print(f"  {emp_id}: {name} - ${salary}")

# ===== CONVERTING TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 9: Converting Tuple Values to Other Types")
print("=" * 60)

tuple_dict = {'data': (1, 2, 3, 4, 5)}
print("Original tuple:", tuple_dict['data'])

# Convert to list
as_list = list(tuple_dict['data'])
print("As list:", as_list)

# Convert to set
as_set = set(tuple_dict['data'])
print("As set:", as_set)

# ===== NESTED TUPLES IN DICTIONARY =====
print("\n" + "=" * 60)
print("EXAMPLE 10: Nested Tuples in Dictionary")
print("=" * 60)

complex_data = {
    'person1': (('John', 'Doe'), (25, 'Engineer')),
    'person2': (('Jane', 'Smith'), (30, 'Manager')),
    'person3': (('Bob', 'Johnson'), (28, 'Developer'))
}

print("Complex data:")
for person_id, (name_tuple, info_tuple) in complex_data.items():
    first, last = name_tuple
    age, position = info_tuple
    print(f"{person_id}: {first} {last}, Age: {age}, Position: {position}")

# ===== USING TUPLES AS DICTIONARY KEYS =====
print("\n" + "=" * 60)
print("EXAMPLE 11: Using Tuples as Dictionary Keys")
print("=" * 60)

# Tuples can be used as keys because they're immutable
location_data = {
    (10, 20): 'Point A',
    (30, 40): 'Point B',
    (50, 60): 'Point C'
}

print("Location data with tuple keys:")
for coords, location in location_data.items():
    print(f"  {coords}: {location}")

# Access by tuple key
print(f"\nLocation at (30, 40): {location_data[(30, 40)]}")

# ===== COUNTING OCCURRENCES IN TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 12: Counting Occurrences in Tuple Values")
print("=" * 60)

results = {
    'test1': (85, 90, 88),
    'test2': (92, 85, 88),
    'test3': (88, 88, 85)
}

print("Test results:", results)

# Count how many times each score appears across all tests
score_count = {}
for test_name, scores in results.items():
    for score in scores:
        score_count[score] = score_count.get(score, 0) + 1

print("Score frequencies:", score_count)

# ===== COMBINING MULTIPLE TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 13: Combining Tuple Values")
print("=" * 60)

sets_data = {
    'set1': (1, 2, 3),
    'set2': (4, 5, 6),
    'set3': (7, 8, 9)
}

print("Original sets:", sets_data)

# Combine all tuples into one
combined_tuple = tuple(item for values in sets_data.values() for item in values)
print("Combined tuple:", combined_tuple)

# Create new dictionary with combined
combined_dict = {'all': combined_tuple}
print("Combined dictionary:", combined_dict)

# ===== COMPARING TUPLE VALUES =====
print("\n" + "=" * 60)
print("EXAMPLE 14: Comparing Tuple Values")
print("=" * 60)

versions = {
    'app1': (1, 0, 0),
    'app2': (1, 5, 0),
    'app3': (2, 0, 1)
}

print("Application versions:", versions)

for app_name, version in versions.items():
    if version >= (2, 0, 0):
        print(f"{app_name} is version 2 or higher: {version}")
    else:
        print(f"{app_name} is version 1.x: {version}")

# ===== MAPPING WITH TUPLE ARITHMETIC =====
print("\n" + "=" * 60)
print("EXAMPLE 15: Tuple Arithmetic in Dictionary")
print("=" * 60)

positions = {'start': (0, 0), 'end': (10, 20)}
offset = (5, 5)

print("Original positions:", positions)

# Add offset to position
new_start = tuple(a + b for a, b in zip(positions['start'], offset))
new_end = tuple(a + b for a, b in zip(positions['end'], offset))

positions['start'] = new_start
positions['end'] = new_end
print("After offset:", positions)