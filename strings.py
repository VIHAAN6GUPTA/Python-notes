# Strings: ordered, immutable, text representation

# Assign age and print using formatted string
age = 25
print(f"Jim is {age} years old.")             # f-string (formatted string literal)
print("The age of Tom is %d" % age)           # old-style formatting
print("Bob is {} years old".format(age))      # str.format() method


# String literals
"Mike"
'Mike'

# Assign a name
name = "Mike"

# String concatenation
phrase = "Mike" + " is my name"

# Append to the existing string using +=
name += " is my name"
print(name)  # Output: mike is my name

# Multiline string using triple quotes
print(""" Mike
      is
      39
      years
      old""")

# Convert to lowercase
print("Mike".lower())  # mike

# Convert to title case (each word starts with capital letter)
print("mike is a man".title())  # Mike Is A Man

# Check if string contains only letters and is not empty
print("Mike".isalpha())     # True

# Check if string contains only letters and/or digits
print("Mike123".isalnum())  # True

# Check if string contains only digits
print("123".isdecimal())    # True

# Check if string is lowercase
print("mike".islower())     # True

# Check if string is uppercase
print("MIKE".isupper())     # True

print("Mike".lower())   # mike
print("mike".upper())   # MIKE
print("mike is a man".title())  # Mike Is A Man

# Check if string starts with substring
print("Mike is here".startswith("Mike"))  # True

# Check if string ends with substring
print("Mike is here".endswith("here"))    # True

# Replace part of string
print("Mike is here".replace("here", "at home"))  # Mike is at home

# Split string into list of words
print("Mike is a man".split())  # ['Mike', 'is', 'a', 'man']

# Remove leading/trailing whitespace
print("   Mike   ".strip())  # "Mike"

# Join characters with a separator
print("-".join("Mike"))  # M-i-k-e
print(" ".join("How are you doing".split()))

# Find index of substring (returns -1 if not found)
print("Mike is a man".find("is"))  # 5

# Get length of string
print(len(name))  # Length of "mike is my name" = 17

# Escape character to include quotes
name = "Be\"au"
print(name[1])  # e

# Slice a string 
name = "Mike is a man"
print(name[2:4])     # ke (from index 2 to 3)
print(name[1::2])    # ik sa a (start at index 1, step 2)
print(name[1::-1])   # iM (reverse till index 0)

# Check if a character or substring is in main string
print('is' in name)  # True

