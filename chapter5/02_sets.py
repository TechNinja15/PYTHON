#Set is a collection of unique items
myset= {1,2,3,4,5,5,5,5}
# print(myset)        #duplicates will be ignored          # Output: {1, 2, 3, 4, 5}
s= set() # to create a empty set
# print(type(s))


# =========================== Methods of Set ===============================

# 1. add() - Adds an element to the set
a = set()
a.add(1)
a.add(2)
print("Set after adding elements:", a)  # Output: {1, 2}

# 2. clear() - Removes all elements from the set
a.clear()
print("Set after clear():", a)  # Output: set()

# 3. copy() - Returns a shallow copy of the set
a = {1, 2, 3}
b = a.copy()
print("Copied set:", b)  # Output: {1, 2, 3}

# 4. difference() - Returns elements in the first set but not in others
a = {1, 2, 3, 4}
b = {3, 4, 5}
print("Difference:", a.difference(b))  # Output: {1, 2}

# 5. difference_update() - Removes elements found in another set from this set
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print("After difference_update:", a)  # Output: {1, 2}

# 6. discard() - Removes an element if present (no error if not)
a = {1, 2, 3}
a.discard(2)
a.discard(5)
print("After discard:", a)  # Output: {1, 3}

# 7. intersection() - Returns common elements between sets
a = {1, 2, 3}
b = {2, 3, 4}
print("Intersection:", a.intersection(b))  # Output: {2, 3}

# 8. intersection_update() - Updates the set with intersection of itself and others
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print("After intersection_update:", a)  # Output: {2, 3}

# 9. isdisjoint() - Returns True if sets have no common elements 
a = {1, 2, 3}
b = {4, 5}
print("Is disjoint:", a.isdisjoint(b))  # Output: True

# 10. issubset() - Returns True if all elements of set are in another set
a = {1, 2}
b = {1, 2, 3}
print("Is subset:", a.issubset(b))  # Output: True

# 11. issuperset() - Returns True if set contains all elements of another set
a = {1, 2, 3}
b = {1, 2}
print("Is superset:", a.issuperset(b))  # Output: True

# 12. pop() - Removes and returns a random element
a = {10, 20, 30}
x = a.pop()
print("Popped element:", x)
print("Set after pop:", a)

# 13. remove() - Removes a specified element (raises error if not found)
a = {1, 2, 3}
a.remove(2)
print("After remove:", a)  # Output: {1, 3}
# a.remove(5)  # This would raise a KeyError

# 14. symmetric_difference() - Returns elements not common to both sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Symmetric difference:", a.symmetric_difference(b))  # Output: {1, 2, 4, 5}

# 15. symmetric_difference_update() - Updates the set with symmetric difference
a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print("After symmetric_difference_update:", a)  # Output: {1, 2, 4, 5}

# 16. union() - Returns all unique elements from both sets
a = {1, 2}
b = {2, 3}
print("Union:", a.union(b))  # Output: {1, 2, 3}

# 17. update() - Adds all elements from another set (or iterable)
a = {1, 2}
b = {3, 4}
a.update(b)
print("After update:", a)  # Output: {1, 2, 3, 4}