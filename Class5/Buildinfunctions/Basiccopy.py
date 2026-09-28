# Exampe 1: Simple list copy using slicing
list1 = [1, 2, 3, 4, 5]
list2 = list1[:]  # Create a copy of list1 using slicing
print("Original list:", list1)
# Example 2: Copy using list()funtion.
list3 =list(list1)
print(list3)

# Example 3: Copy using copy module.

import copy
list4 = copy.copy(list2)
print(list4)

# Exampe 4 Copy using append in a loop.
list5 = []
for item in list3:
	list5.append(item)
print(list5)

#Example 5: Copy using list comprehension.
list6 = [x for x in list]
print(list6)

#Example 6: copy using extend()

list7= []
list.extend(list2)
print(list7)



