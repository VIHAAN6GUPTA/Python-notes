# Operator Overloading Example
# Operator overloading lets you define how operators like >, <, +, etc., behave for objects of your custom class.


# Define Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name  # Dog's name
        self.age = age    # Dog's age

    # Overload the greater than (>) operator
    def __gt__(self, other):
        # Return True if this dog's age is greater than the other dog's age
        return True if self.age > other.age else False

# Create two Dog objects
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

# Use the overloaded > operator to compare their ages
print(roger > syd)  # Output: True, because 8 > 7

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload + operator to add ages
    def __add__(self, other):
        return self.age + other.age

dog1 = Dog("Roger", 8)
dog2 = Dog("Syd", 5)

print(dog1 + dog2)  # Output: 13 (8 + 5)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload == operator to compare two dogs
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

dog1 = Dog("Roger", 8)
dog2 = Dog("Roger", 8)
dog3 = Dog("Syd", 5)

print(dog1 == dog2)  # True
print(dog1 == dog3)  # False

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload str() to return a custom string
    def __str__(self):
        return f"{self.name} is {self.age} years old"

dog = Dog("Roger", 8)
print(dog)  # Output: Roger is 8 years old

# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() reespond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator