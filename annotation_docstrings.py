# ---------- Docstrings ----------

# This is a function with a docstring explaining what it does.
def increment(n):
    """Increment a number"""
    return n + 1

# A module-level docstring (normally at the top of a Python file)
"""Dog module
This module does ... bla bla bla and provides following classes:
Dog
"""

# A class with its own docstring
class Dog:
    """A class representing a dog"""

    def __init__(self, name, age):
        """Initialise a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("woof")

# ---------- Annotations ----------

# Function annotations: specify the expected input and return types
def increment1(n: int) -> int:
    return n + 1

# Variable annotation: explicitly states that 'count' is an integer
count: int = 0

# Note: Python doesn't enforce these annotations—they are hints for developers and tools

# ---------- Exceptions in Python ----------

# General structure of try-except-else-finally block:
try:
    # Code that might raise an exception
    pass
except ZeroDivisionError:
    # Handle division by zero
    pass
except ValueError:
    # Handle value-related errors
    pass
else:
    # This block runs if no exception was raised in the try block
    pass
finally:
    # This block always runs, no matter what
    pass


# Example: Handling a ZeroDivisionError
try:
    result = 2 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print('Cannot divide by zero')  # Error is handled here
    result = 0  # Set result to a default value to avoid undefined variable
finally:
    print("Finished handling the exception")  # This will always execute

# Continue with the program
print(result)  # Output: 0
