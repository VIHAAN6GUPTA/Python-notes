# List: ordered, mutable, allows duplicate elements

# A list with mixed data types
dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

# Check if "Beau" is in the list
print("Beau" in dogs)  # Output: False

# Accessing first element
print(dogs[0])  # Output: Roger

# Modifying an element at index 2
dogs[2] = "Beau"
print(dogs[2])  # Output: Beau

# Slicing from index 2 to 3 (not including index 4)
print(dogs[2:4])  # Output: ['Beau', True]
# It goes from beginning to end by stepping 1
print(dogs[1::1])  # Output: ['Roger', 1, 'Beau', True, 'Quincy', 7]
# It goes from beginning to end by stepping 2
print(dogs[1::2]) # Output: ['Roger', 'Beau', 'Quincy']  1, True and 7 is not printed
# Adding a negative integer reverses the list eg: [1::-1]

# Length of the list
print(len(dogs))  # Output: 6

# Append adds a single item to the end
dogs.append("Judah")

# Extend adds multiple items to the list
dogs.extend(["Bob", 5])

# += also extends the list
dogs += ["Jack"]

# Remove the first occurrence of a value
dogs.remove("Quincy")

# Clear the list
# dogs.clear()
# print(dogs)

# Pop removes and returns the last item
print(dogs.pop())  # Output: Jack

# Insert "Test" at index 2
dogs.insert(2, "Test")

# View final list
print(dogs)

# Reverse the list
dogs.reverse()
print(dogs)

# A list of names 
name = ["Roger", "Syd", "bob", "Beau", "Quincy"]  

# Make a copy using slicing
namecopy = name[:]  # [:] This slices it from beginning to end

# Sort the original list in-place, ignoring case
name.sort(key = str.lower)
print(name)       # Sorted list

# Print the unsorted copy
print(namecopy)   # Original unsorted copy

# Print a new sorted list (ignoring case) without changing the original list
print(sorted(name, key = str.lower))  # Returns a new sorted list (case-insensitive)

mylist = [0] * 5  # Creates a list with 5 elements, all initialized to 0
print(mylist)     # Output: [0, 0, 0, 0, 0]

# Create a list named 'items' with two elements: 1 and 2
items = [1, 2]

# Print the memory address (unique identifier) of the 'items' list object
print(id(items))

# List compressions

# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Using list comprehension to create a new list with squares of each number
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)  # Output: [1, 4, 9, 16, 25]

# Doing the same using a for loop and appending squares to a new list
numbers_powers_2 = []
for n in numbers:
    numbers_powers_2.append(n**2)  # Append square of each number

# Using the map function and a lambda (anonymous function) to get squares
numbers_powers1_2 = list(map(lambda n: n**2, numbers))  # Convert map object to list

# List of numbers
nums = [1, 2, 3, 4, 5, 6]

# Unpacking: all elements except the last go into 'beginning', and the last goes into 'last'
*beginning, last = nums

# 'beginning' is a list containing all elements except the last one: [1, 2, 3, 4, 5]
print(beginning)

# 'last' is the last element of the list: 6
print(last)
