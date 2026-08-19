# tuple of vowels
vowels = ("a", "e", "i", "o", "u")

fSet = frozenset(vowels)
print("The frozen set is:", fSet)
print("The empty frozen set is:", frozenset())

# frozensets are immutable
# fSet.add("v")  # This would raise an AttributeError