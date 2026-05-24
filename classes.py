# Define a base class called Animal
class Animal:
    # Method that prints a walking message
    def walk(self):
        print("Walking..")


# Define a subclass Dog that inherits from Animal
class Dog(Animal):
    # Constructor (__init__) to initialize Dog object with name and age
    def __init__(self, name, age):
        self.name = name  # Assign the name attribute
        self.age = age    # Assign the age attribute

    # Method for the dog to bark
    def bark(self):
        print("woof")


# Create an instance (object) of Dog with name "Roger" and age 8
roger = Dog("Roger", 8)

# Print the type of the object (should be <class '__main__.Dog'>)
print(type(roger))

# Access and print the name attribute of the Dog object
print(roger.name)

# Access and print the age attribute of the Dog object
print(roger.age)

# Call the bark method (defined in Dog class)
roger.bark()

# Call the walk method (inherited from Animal class)
roger.walk()
