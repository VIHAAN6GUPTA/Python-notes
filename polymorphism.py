# Polymorphism Example

# Define Dog class with an 'eat' method
class Dog:
    def eat(self):
        print("eating dog food")

# Define Cat class with an 'eat' method
class Cat:
    def eat(self):
        print("eating cat food")

# Create instances of Dog and Cat
animal1 = Dog()
animal2 = Cat()

# Call the 'eat' method on both instances
animal1.eat()  # Output: eating dog food
animal2.eat()  # Output: eating cat food

# Both Dog and Cat have the same method name: eat().

# Python allows calling eat() on either object without knowing its exact class — this is polymorphism.