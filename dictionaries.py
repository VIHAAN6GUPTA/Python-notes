# Dictionary: Key-Value, Unordered, mutable

# Creating a dictionary with key-value pairs
dog = {"name": "Roger", "age": 8, "color": "green"}

# Accessing a value using a key
print(dog["name"])  # Output: Roger

# Updating a value
dog["name"] = "Syd"
print(dog)  # Output: {'name': 'Syd', 'age': 8, 'color': 'green'}

# Accessing a value using get (safe method, avoids KeyError)
print(dog.get("color"))  # Output: green

# Check if a key exists in the dictionary
print("color" in dog)  # Output: True

# Get all keys, values, and key-value pairs
print(list(dog.keys()))    # Output: ['name', 'age', 'color']
print(list(dog.values()))  # Output: ['Syd', 8, 'green']
print(list(dog.items()))   # Output: [('name', 'Syd'), ('age', 8), ('color', 'green')]

# Add a new key-value pair
dog["favourite food"] = "Meat"

# Delete a key-value pair
del dog["color"]

# Make a copy of the dictionary
dogcopy = dog.copy()
dogcopy["City"] = "Boston"
print(dogcopy)  # the main dog dictionary does not change even if we modify dogcopy

# Remove a specific item and return its value
print(dog.pop("name"))  # Output: Syd

# Print current dictionary
print(dog)  # Output: {'age': 8, 'favourite food': 'Meat'}

# Remove and return the **last inserted item** as a (key, value) tuple
print(dog.popitem())  # Output: ('favourite food', 'Meat')

# Final dictionary state
print(dog)  # Output: {'age': 8}

# Create a dictionary
my_dict = dict(name = "Mary", age = 27, City = "Boston")
print(my_dict)

for key, value in my_dict.items():
    print(key, value)

# Update the dictionary with new data
my_dict2 = dict(name = "Max", age = 25, City = "New york")    
my_dict.update(my_dict2)
print(my_dict)

# First dictionary with two key-value pairs
dict_a = {'a': 1, 'b': 2}

# Second dictionary with two different key-value pairs
dict_b = {'c': 3, 'd': 4}

# Unpacking both dictionaries using ** to merge them into a new dictionary
# **dict_a unpacks: 'a': 1, 'b': 2
# **dict_b unpacks: 'c': 3, 'd': 4
my_dict = {**dict_a, **dict_b}

# Print the combined dictionary
print(my_dict)
