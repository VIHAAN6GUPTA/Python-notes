# Check if a person is an adult or a child based on age
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")

# Check the age category using multiple conditions
age1 = 25
if age1 >= 18:
    print("You are an adult")
elif age1 > 12:  # Corrected from 'age' to 'age1'
    print("You are a teen")
elif age1 > 1:
    print("You are a child")
else:
    print("You are a baby")

# Function to check if a person is an adult (returns True if age is over 18)
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# Shorter version of the same function using a ternary operator
def is_adult2(age):
    return True if age > 18 else False
   