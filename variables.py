# Assigning a string value to the variable 'name'
name = "Jim"

# Printing the value of 'name'
print(name)

# Printing the type of 'name' (should output <class 'str'>)
print(type(name))

# Checking if the type of 'name' is exactly a string using '=='
print(type(name) == str)

# Checking if 'name' is an instance of the string class using 'isinstance()'
print(isinstance(name, str))


# Assigning an integer value to the variable 'age'
age = 25
# Print the number of bits needed to represent the integer 25 in binary (excluding the sign and leading zeros)
print(age.bit_length())

# Converting 'age' to a float (from int to float)
age = float(25)

# Assigning a floating-point number to the variable 'gpa'
gpa = 2.9


# Assigning a string number to the variable 'num'
num = "20"

# Converting the string "20" to an integer and reassigning it to 'num'
num = int("20")

# Define a complex number using a literal
complex = 2 + 3j  # 'j' is the imaginary unit in Python

# Define a complex number using the complex() constructor
num2 = complex(2, 3)  # This creates the same complex number: 2 + 3j

# Accessing the real and imaginary parts
print(num2.real, num2.imag)  # Output: 2.0 3.0


# Operators
print(1 + 1)    # 2       → Addition
print(2 - 1)    # 1       → Subtraction
print(2 * 2)    # 4       → Multiplication
print(4 / 2)    # 2.0     → Division (returns float)
print(4 % 3)    # 1       → Modulus (remainder)
print(4 ** 2)   # 16      → Exponentiation (4 to the power of 2)
print(5 // 2)   # 2       → Floor division (rounds down)

# Compound assignment
age = 8
age += 6       # Adds 6 to age (8 + 6)
print(age)     # 14

# Comparison operators
a = 1
b = 2
print(a == b)   # False   → Equality
print(a < b)    # True    → Less than
print(a != b)   # True    → Not equal
print(a >= b)   # False   → Greater than or equal


# Boolean operators
condition1 = True
condition2 = False

print(not condition1)           # Output: False
print(condition1 and condition2)  # Output: False
print(condition1 or condition2)   # Output: True

print(0 or 1)             # 1
print(False or 'hey')     # 'hey'
print('hi' or 'hey')      # 'hi'
print([] or False)        # False
print(False or [])        # []

print(0 and 1)            # 0
print(1 and 0)            # 0
print(False and 'hey')    # False
print('hi' and 'hey')     # 'hey'
print([] and False)       # []
print(False and [])       # False
