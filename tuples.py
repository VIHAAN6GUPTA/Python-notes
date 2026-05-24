# A tuple is like a list, but **immutable** (unchangeable), allows duplicate elements

names = ("Roger", "Syd", "Beau")

# Accessing elements by index (like a list)
print(names[0])  # Output: Roger

# Finding the index of an element
print(names.index("Roger"))  # Output: 0

# Getting the length of the tuple
print(len(names))  # Output: 3

# Check if an item is in the tuple
print("Roger" in names)  # Output: True

# Slicing a tuple (same as with lists)
print(names[0:2])  # Output: ('Roger', 'Syd')

# Sorting the tuple (returns a new sorted list)
print(sorted(names))  # Output: ['Beau', 'Roger', 'Syd']

# Concatenating tuples (creates a new tuple)
newTuple = names + ("Tina", "Mike")
print(newTuple)  # Output: ('Roger', 'Syd', 'Beau', 'Tina', 'Mike')

# Convert tuple to list
my_list = list(names)
print(my_list)
# Convert list back to tuple
names2 = tuple(my_list)
print(names2)

# Unpack a tuple
my_tuple = ("Bob", 5, "Boston")
name, age, city = my_tuple
print(name)
print(age)
print(city)

# Compare list and tuple
import sys
my_list1 = [0, 1, 2, 3, 4, 5]
my_tuple1 = (0, 1, 2, 3, 4, 5)
print(sys.getsizeof(my_list1), "bytes")
print(sys.getsizeof(my_tuple1), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number = 1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number = 1000000))

# A tuple containing 3 elements
my_tuple = (1, 2, 3)

# A list containing 3 elements
my_list = [4, 5, 6]

# A set containing 2 elements
my_set = {7, 8}

# Unpacking all elements from tuple, list, and set into a new list
# *my_tuple unpacks (1, 2, 3)
# *my_list unpacks [4, 5, 6]
# *my_set unpacks {7, 8} — note: set order is not guaranteed
new_list = [*my_tuple, *my_list, *my_set]

# Printing the final merged list
print(new_list)
