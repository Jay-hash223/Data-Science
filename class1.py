# Different Dta Types in Python
# Immutable: int,float,str,tuple,frozenset,etc.
# Mutable: list,dict,set,bytearray,etc.
# Non Data types.
array = [1,2,3,4,5,6,7]
print(type(array))
matrix = [[1,2,3]],[4,5,6]
print (type(matrix))
vector = (1,2,3,4,5)
data_set = {1,2,3,4,5}

print(type(data_set))

# Next Dictionary:
dictionary = {"name": "Ram","age":29}
print(type(dictionary))
print("")
# The above is non data type one.

x = None
print(type(x))
print(x)

# A key difference between bytes and strings is that bytes are immutable and do not support most string methods directily.
# Example: you can not concatenate a nytes obejects withe a string without explicit conversion.

# Other one:

b = b"namaste"

print(type(b))

print(b)
print(b.decode("utf-8"))
print(type(b.decode("utf-8")))
print("")

#byte array

ba = bytearray([55,56,66])
print(type(ba))
print(ba)

print("")

# memoryview

mv = memoryview(b"namaste")
print(type(mv))
print(mv.tobytes())
print(mv.tobytes().decode("utf-8"))
print(type(mv.tobytes().decode("utf-8")))
print("")


# Unlike Java,Python does not have a built-in-arrat tyoe for genereal use. The closet built-in structure is list,which is more flexiable than Java arrays because it can hold elements of deifferent types and can change size.

# Range:
# Range is used to generate a sequence of numbers.
# Range is also a datat type in python.

# Example:

r = range(4)
print(type(r))
print(list(r))
print("")

#Frozen set is a iimutable version of a set.

# Example:

fs = frozenset([1,2,3,4,5])
print(type(fs))
print(fs)
print("")