# ---------- Lambda Functions ----------

# A lambda function that takes one input and returns its double
lambda num: num * 2

# A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print(multiply(2, 4))  # Output: 8

# A list of 2D points (tuples with x and y coordinates)
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# Sort points by the second value (y-coordinate) using lambda function
points2D_sorted = sorted(points2D, key=lambda x: x[1])
# Output: [(5, -1), (15, 1), (1, 2), (10, 4)]
# Explanation: Sorts based on y-values: -1, 1, 2, 4

# Sort points by the sum of x and y (x + y)
points2D_sorted1 = sorted(points2D, key=lambda x: x[0] + x[1])
# Output: [(1, 2), (5, -1), (10, 4), (15, 1)]
# Explanation: x+y values: 3, 4, 14, 16 → sorted as: 3, 4, 14, 16

# Original list remains unchanged (because `sorted()` returns a new list)
print(points2D)           # [(1, 2), (15, 1), (5, -1), (10, 4)]

# Sorted by y-coordinate
print(points2D_sorted)    # [(5, -1), (15, 1), (1, 2), (10, 4)]

# Sorted by sum of x and y
print(points2D_sorted1)   # [(1, 2), (5, -1), (10, 4), (15, 1)]


# ---------- map() Function ----------

numbers = [1, 2, 3]

# Regular function to double a number
def double(a):
    return a * 2

# Using map with a regular function
result = map(double, numbers)

# Using map with a lambda function (same result)
result = map(lambda a: a * 2, numbers)

# map returns a map object, so convert to list
print(list(result))  # Output: [2, 4, 6]

# ---------- filter() Function ----------

numbers1 = [1, 2, 3, 4, 5, 6]

# Regular function to check if a number is even
def isEven(n):
    return n % 2 == 0

# Using filter with a regular function
result1 = filter(isEven, numbers1)

# Using filter with a lambda function (same result)
result1 = filter(lambda n: n % 2 == 0, numbers1)

# Convert filter object to list
print(list(result1))  # Output: [2, 4, 6]
print([x for x in numbers1 if x%2 == 0])

# ---------- Reduce Function ----------

expenses = [('Dinner', 80), ('Car repair', 120)]

# Traditional way to sum up expenses
sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)  # Output: 200

from functools import reduce

expenses1 = [('Dinner', 80), ('Car repair', 120)]

# Using reduce with lambda to sum expenses
# a and b are tuples; a[1] and b[1] are the costs
# This line is incorrect and will raise an error since a and b are tuples, not numbers
# You need to extract values differently or use a more appropriate structure
# Here's the corrected version:

sum1 = reduce(lambda acc, item: acc + item[1], expenses1, 0)
print(sum1)  # Output: 200

# ---------- Recursion Example ----------

# Recursive function to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))  # Output: 6
print(factorial(4))  # Output: 24
print(factorial(5))  # Output: 120

# ---------- Decorators ----------

import functools  # Needed for @functools.wraps to preserve function metadata

# Decorator that logs before and after a function is called
def logtime(func):
    @functools.wraps(func)  # Preserves original function name and docstring
    def wrapper(*args, **kwargs):
        print("Start")  # Runs before the function
        val = func(*args, **kwargs)  # Calls the original function
        print("End")  # Runs after the function
        return val  # Returns the result of the original function
    return wrapper  # Returns the new wrapped function

# Apply logtime decorator to hello()
@logtime
def hello():
    print("hello")

hello()
# Output:
# Start
# hello
# End

# Apply logtime decorator to add5()
@logtime
def add5(x):
    return x + 5

val = add5(10)
print(val)  # Output: 15

# Check that metadata of the function is preserved
print(help(add5))           # Help on the original function (thanks to functools.wraps)
print(add5.__name__)        # Prints 'add5', not 'wrapper'

# Decorator factory: creates a decorator that repeats a function `num_times` times
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):  # Repeat function call
                result = func(*args, **kwargs)
            return result  # Return the result of the last function call
        return wrapper
    return decorator_repeat

# Apply repeat decorator to greet(), to repeat it 3 times
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet('Alex')  # Will print "Hello Alex" three times

# Debug decorator: logs function name, arguments, and return value
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Convert arguments to string representations
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")  # Before function call
        result = func(*args, **kwargs)  # Call the original function
        print(f"{func.__name__!r} returned {result!r}")  # After function call
        return result
    return wrapper

# Another decorator to mark function start and end
def start_end_decorator_4(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')  # Before function
        result = func(*args, **kwargs)  # Original function
        print('End')  # After function
        return result
    return wrapper

# Decorate say_hello() with both debug and start_end_decorator_4
@debug  # Outer decorator (executes first)
@start_end_decorator_4  # Inner decorator (executes second)
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# Call the decorated function
say_hello(name='Alex')

# Output:
# Calling say_hello(name='Alex')    <-- debug decorator before
# Start                             <-- start_end_decorator_4 before
# Hello Alex                        <-- actual function logic
# End                               <-- start_end_decorator_4 after
# 'say_hello' returned 'Hello Alex' <-- debug decorator after

# Define a decorator class to count how many times a function is called
class CountCalls:
    def __init__(self, func):
        # Store the function that is being decorated
        self.func = func
        # Initialize the counter for how many times the function is called
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        # This special method makes the object callable like a function
        # Each time the function is called, increment the counter
        self.num_calls += 1
        # Print how many times the function has been called so far
        print(f"This is executed {self.num_calls} times")
        # Call the original function and return its result
        return self.func(*args, **kwargs)

# Use the CountCalls class as a decorator for the say_hello function
@CountCalls
def say_hello():
    print('Hello')

# Call the decorated function twice
say_hello()
say_hello()

# ---------- Generators ----------

# Define a simple generator function using 'yield'
def mygenerator():
    yield 1
    yield 2
    yield 3

# Create a generator object from the function
g = mygenerator()

# Use next() to get the next value from the generator
value = next(g)
print(value)  # Output: 1

value = next(g)
print(value)  # Output: 2

value = next(g)
print(value)  # Output: 3

# After exhausting the generator, the remaining calls do not produce more values
# sum() and sorted() here operate on an exhausted generator, so the results are empty
print(sum(g))      # Output: 0 (g is exhausted after 3 yields above)
print(sorted(g))   # Output: [] (nothing left to sort)

# ------------------------------

# Generator function to count down from a number
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# Create a generator object for countdown
cd = countdown(3)

# Fetch values one by one using next()
print(next(cd))  # Output: Starting \n 3
print(next(cd))  # Output: 2
print(next(cd))  # Output: 1

# ------------------------------

# Normal function (not a generator) that returns a list of numbers from 0 to n-1
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Use the function and print result
print(firstn(10))              # Output: [0, 1, 2, ..., 9]
print(sum(firstn(10)))         # Output: 45

# ------------------------------

# Generator version of the above function (memory efficient)
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Sum over the generator directly without creating a list
print(sum(firstn_generator(10)))   # Output: 45

# ------------------------------

# Generator for Fibonacci sequence up to a limit
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Create the generator and iterate through it using a for loop
fib = fibonacci(10)
for i in fib:
    print(i)  # Output: 0 1 1 2 3 5 8

# ------------------------------

# Generator expression for even numbers from 0 to 9
mygenerator = (i for i in range(10) if i % 2 == 0)

# List comprehension version (creates a list in memory)
mylist = [i for i in range(10) if i % 2 == 0]

# Convert the generator to a list and print
print(list(mygenerator))  # Output: [0, 2, 4, 6, 8]
print(mylist)             # Output: [0, 2, 4, 6, 8]
