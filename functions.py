# Function with a default parameter
def hello(name="my friend"):
    print("Hello " + name)

# Calling hello with different arguments
hello("Mike")      # Output: Hello Mike
hello("Quincy")    # Output: Hello Quincy
hello()            # Output: Hello my friend

# Function with two parameters: name and age
def hello2(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")

hello2("Beau", 39)  # Output: Hello Beau, you are 39 years old


# Function that tries to change an integer (immutable)
def change(value):
    value = 2  # This change only affects the local copy inside the function

val = 1
change(val)
print(val)  # Output: 1 (no change to original)


# Function that changes a dictionary (mutable)
def change1(value1):
    value1["name"] = "Syd"  # This change affects the original dictionary

val1 = {"name": "Beau"}
change1(val1)
print(val1)  # Output: {'name': 'Syd'}


# Function that returns multiple values
def hi(name1):
    print("Hello " + name1)
    return name1, "Mike", 8

print(hi("Syd"))
# Output:
# Hello Syd
# ('Syd', 'Mike', 8)


# Function with early return if name is empty
def hi1(name2):
    if not name2:
        return  # Return None if name2 is empty or None
    print("Hello " + name2)

hi1("Beau")  # Output: Hello Beau


# Function using a nested function to print each word
def talk(phrase):
    def say(word):  # Inner function to print each word
        print(word)
    
    words = phrase.split(' ')  # Split the phrase into words
    for word in words:
        say(word)  # Call inner function for each word

talk('I am going to buy milk')
# Output:
# I
# am
# going
# to
# buy
# milk


# Function with a nested function and nonlocal variable
def count():
    count = 0  # Outer variable

    def increment():
        nonlocal count  # Allows access to the outer variable
        count = count + 1
        print(count)

    increment()

count()
# Output: 1


# Function that returns an incrementing function (closure)
def counter():
    count = 0

    def increment():
        nonlocal count  # Keeps track of count across calls
        count = count + 1
        return count
    
    return increment

increment = counter()

print(increment())  # Output: 1
print(increment())  # Output: 2
