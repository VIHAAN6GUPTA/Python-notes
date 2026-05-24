# Ask the user for their age (input is always returned as a string)
age = input("What is your age? ")

# Print a message including the age using string concatenation
print("Your age is " + age)


# Print multiple strings separated by " | " instead of default space
print("Python", "Java", "C++", sep=" | ")  # Output: Python | Java | C++

# Print without adding a newline (by default, print ends with a newline)
print("Loading", end="...")  # The next print continues on the same line
print(" Done!")              # Output: Loading... Done!


# Print a string that includes double quotes using escape character \"
print("This is how you write \"double quotes\" in a string.")  
# Output: This is how you write "double quotes" in a string.

# Print multiple lines using \n (newline character)
print("Line1\nLine2\nLine3")  
# Output:
# Line1
# Line2
# Line3

# Print tabular data using \t (tab character)
print("Item\tPrice")          
print("Milk\t₹25.00\nBread\t₹15.00")  
# Output:
# Item    Price
# Milk    ₹25.00
# Bread   ₹15.00


# Define variables for name and age
name = 'Mike'
age = 29

# Print a multiline welcome message using an f-string and triple quotes
print(f"""Hello {name},

Welcome to our platform!

Your age is {age}, and your profile has been created successfully.

Thank you!
""")
# Output:
# Hello Mike,
#
# Welcome to our platform!
#
# Your age is 29, and your profile has been created successfully.
#
# Thank you!
