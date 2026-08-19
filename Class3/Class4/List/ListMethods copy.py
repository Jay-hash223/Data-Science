# ===== LIST METHODS - COMPREHENSIVE EXAMPLES =====
print("=" * 70)
print("LIST METHODS IN PYTHON - COMPLETE GUIDE")
print("=" * 70)

# ===== 1. APPEND() - Add single element to end =====
print("\n" + "=" * 70)
print("1. APPEND() - Add element to end of list")
print("=" * 70)

Mohan = [3, 1, 4]
print("Original list:", Mohan)
Mohan.append(5)
print("After append(5):", Mohan)
Mohan.append(10)
print("After append(10):", Mohan)

# ===== 2. INSERT() - Insert at specific position =====
print("\n" + "=" * 70)
print("2. INSERT() - Insert element at specific index")
print("=" * 70)

list_insert = [1, 2, 4, 5]
print("Original list:", list_insert)
list_insert.insert(2, 3)  # Insert 3 at index 2
print("After insert(2, 3):", list_insert)
list_insert.insert(0, 0)  # Insert at beginning
print("After insert(0, 0):", list_insert)

# ===== 3. REMOVE() - Remove first occurrence =====
print("\n" + "=" * 70)
print("3. REMOVE() - Remove first occurrence of value")
print("=" * 70)

list_remove = [3, 1, 4, 5, 4, 4]
print("Original list:", list_remove)
list_remove.remove(4)  # Removes first 4
print("After remove(4):", list_remove)
list_remove.remove(1)
print("After remove(1):", list_remove)

# ===== 4. POP() - Remove and return element at index =====
print("\n" + "=" * 70)
print("4. POP() - Remove and return element (default: last)")
print("=" * 70)

Mohan = [3, 1, 4, 5, 10]
print("Original list:", Mohan)
popped = Mohan.pop()  # Removes last element
print(f"Popped element: {popped}, Remaining list: {Mohan}")
popped = Mohan.pop(1)  # Remove element at index 1
print(f"Popped element at index 1: {popped}, Remaining list: {Mohan}")

# ===== 5. CLEAR() - Remove all elements =====
print("\n" + "=" * 70)
print("5. CLEAR() - Remove all elements from list")
print("=" * 70)

list_clear = [1, 2, 3, 4, 5]
print("Original list:", list_clear)
list_clear.clear()
print("After clear():", list_clear)

# ===== 6. SORT() - Sort in ascending/descending order =====
print("\n" + "=" * 70)
print("6. SORT() - Sort list elements")
print("=" * 70)

Mohan = [3, 1, 4, 2, 5]
print("Original list:", Mohan)
Mohan.sort()
print("After sort():", Mohan)

Mohan = [3, 1, 4, 2, 5]
Mohan.sort(reverse=True)
print("After sort(reverse=True):", Mohan)

# Sort strings
words = ['banana', 'apple', 'cherry', 'date']
words.sort()
print("Sorted words:", words)

# Sort by length
words_by_length = ['banana', 'apple', 'cherry', 'date']
words_by_length.sort(key=len)
print("Sorted by length:", words_by_length)

# ===== 7. REVERSE() - Reverse list order =====
print("\n" + "=" * 70)
print("7. REVERSE() - Reverse list elements")
print("=" * 70)

Mohan = [1, 2, 3, 4, 5]
print("Original list:", Mohan)
Mohan.reverse()
print("After reverse():", Mohan)

# ===== 8. COPY() - Create shallow copy of list =====
print("\n" + "=" * 70)
print("8. COPY() - Create copy of list")
print("=" * 70)

Mohan = [3, 1, 4]
print("Original list:", Mohan)

# Method 1: Using copy()
Mohan_copy1 = Mohan.copy()
print("Copy using copy():", Mohan_copy1)

# Method 2: Using slicing
Mohan_copy2 = Mohan[:]
print("Copy using slicing [:]:", Mohan_copy2)

# Method 3: Using list()
Mohan_copy3 = list(Mohan)
print("Copy using list():", Mohan_copy3)

# Demonstrate difference between copy and reference
Mohan.append(100)
print("\nAfter appending 100 to original:")
print("Original list:", Mohan)
print("Copy (unchanged):", Mohan_copy1)

# ===== 9. INDEX() - Find index of element =====
print("\n" + "=" * 70)
print("9. INDEX() - Find index of element")
print("=" * 70)

list_index = [10, 20, 30, 40, 30, 50]
print("List:", list_index)
print("Index of 30:", list_index.index(30))  # Returns first occurrence
print("Index of 40:", list_index.index(40))
print("Index of 10:", list_index.index(10))

# ===== 10. COUNT() - Count occurrences of element =====
print("\n" + "=" * 70)
print("10. COUNT() - Count occurrences of element")
print("=" * 70)

list_count = [1, 2, 3, 2, 2, 4, 2, 5]
print("List:", list_count)
print("Count of 2:", list_count.count(2))
print("Count of 1:", list_count.count(1))
print("Count of 10:", list_count.count(10))

# ===== 11. EXTEND() - Add multiple elements =====
print("\n" + "=" * 70)
print("11. EXTEND() - Add multiple elements from iterable")
print("=" * 70)

list_extend = [1, 2, 3]
print("Original list:", list_extend)
list_extend.extend([4, 5, 6])
print("After extend([4, 5, 6]):", list_extend)

list_extend.extend('abc')
print("After extend('abc'):", list_extend)

# ===== 12. NESTED LISTS - List of lists =====
print("\n" + "=" * 70)
print("12. NESTED LISTS - Lists containing lists")
print("=" * 70)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list (matrix):")
for row in nested_list:
    print(row)

print("\nAccessing elements:")
print("Element at [0][0]:", nested_list[0][0])
print("Element at [1][2]:", nested_list[1][2])
print("Element at [2][1]:", nested_list[2][1])

print("\nIterating nested list:")
for sublist in nested_list:
    for item in sublist:
        print(item, end=' ')
print()

# ===== 13. MATRIX ADDITION =====
print("\n" + "=" * 70)
print("13. MATRIX ADDITION - Add two matrices")
print("=" * 70)

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix Addition Result:")
for row in result:
    print(row)

# ===== 14. MATRIX MULTIPLICATION =====
print("\n" + "=" * 70)
print("14. MATRIX MULTIPLICATION")
print("=" * 70)

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_mult = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Matrix 1:", m1)
print("Matrix 2:", m2)

for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            result_mult[i][j] += m1[i][k] * m2[k][j]

print("Matrix Multiplication Result:")
for row in result_mult:
    print(row)

# ===== 15. LIST COMPREHENSION - Create lists efficiently =====
print("\n" + "=" * 70)
print("15. LIST COMPREHENSION - Create lists efficiently")
print("=" * 70)

# Square of numbers
squares = [x**2 for x in range(1, 6)]
print("Squares of 1-5:", squares)

# Even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers 1-10:", evens)

# Flattened list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print("Flattened nested list:", flattened)

# ===== 16. LIST METHODS SUMMARY =====
print("\n" + "=" * 70)
print("16. QUICK REFERENCE - List Methods Summary")
print("=" * 70)

print("""
append()      - Add element to end
insert()      - Insert at specific position
remove()      - Remove first occurrence
pop()         - Remove and return element
clear()       - Remove all elements
sort()        - Sort elements
reverse()     - Reverse order
copy()        - Create shallow copy
index()       - Find index of element
count()       - Count occurrences
extend()      - Add multiple elements

Examples complete!
""")
