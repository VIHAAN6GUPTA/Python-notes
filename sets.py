# Sets: unordered, mutable (except frozenset), no duplicates

set1 = {"Roger", "Mike", 1, 2, 3, 4, 5, 6}
set2 = {"Roger", "Luna", 1, 2, 3, 9, 10}

# Check if "Roger" is in set1
print("Roger" in set1)

# Union of set1 and set2 (all unique elements from both)
mod = set1 | set2
print(mod)

# Union of two sets: odds and evens
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
union = odds.union(evens)  # All elements from both sets (no duplicates)
print(union)

# Intersection of set1 and set2 (common elements)
intersect = set1 & set2
print(intersect)

# Intersection of odds and evens (should be empty as they have no common elements)
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
intersection = odds.intersection(evens)
print(intersection)

# Difference: elements in set1 but not in set2
mod = set1 - set2
print(mod)

# Same as above using difference() method
diff = set1.difference(set2)
print(diff)

# Symmetric difference: elements in either set1 or set2 but not in both
diff2 = set2.symmetric_difference(set1)
print(diff2)

# Check if set1 is a strict subset of set2
mod = set1 < set2
print(mod)

# Check subset/superset/disjoint relationships
setA = {1, 2, 3, 4, 5, 6, 7}
setB = {1, 2, 3}
print(setA.issubset(setB))     # False: A is not a subset of B
print(setA.issuperset(setB))   # True: A contains all elements of B
print(setA.isdisjoint(setB))   # False: A and B share common elements

# Adding elements to set1 (1 and 2 are already present, so no change)
set1.add(1)
set1.add(2)
print(set1)

# Removing an element from set1
set1.remove(2)
print(set1)

# Remove and return a random element from set1
print(set1.pop())

# Convert set1 to a list (useful when ordering is needed)
print(list(set1))

# Copying setB into setA, then modifying setB
setA = setB.copy()  # setA is now {1, 2, 3}
setB.add(7)         # setB is now {1, 2, 3, 7}
print(setA)         # setA remains unchanged
print(setB)

# Frozenset: an immutable version of a set
a = frozenset([1, 2, 3, 4])
# a.add(5)  # This will raise an error because frozenset is immutable
print(a)
