s = {1, 2}
s.add(3)
print(s)
s.update([4, 5])
print(s)
s.remove(4)
print(s)
s.discard(10)  # no error
print(s)
s.clear()
print(s)

# Means we can add single element using add() and multiple elements using update() method.
# Can also remove single element using remove() and discard() method.
# can remove all elements using clear() method.
# can also use pop() method to remove and return an arbitrary element from the set.
# can also use copy() method to create a shallow copy of the set.
# can also use difference() method to return a new set with elements in the set that are not in the other set.
# can also use difference_update() method to remove all elements of another set from this set.
# can also use intersection() method to return a new set with elements common to the set and another set.
# can also use intersection_update() method to remove all elements of the set that are not in another set.
# can also use isdisjoint() method to return True if the set has no elements in common with another set.
# can also use issubset() method to return True if the set is a subset of another set.
# can also use issuperset() method to return True if the set is a superset of another set.
# can also use pop() method to remove and return an arbitrary element from the set.

