import random

# Generate a random float number between 0 and 1
a = random.random()
print(a)

# Generate a random float number between 1 and 10
b = random.uniform(1, 10)
print(b)

# Generate a random integer between 1 and 10 (inclusive)
c = random.randint(1, 10)
print(c)

# Generate a random integer between 1 and 9 (10 is exclusive)
d = random.randrange(1, 10)
print(d)

# Generate a number from a normal distribution with mean=0 and std deviation=1
e = random.normalvariate(0, 1)
print(e)

# Create a list of letters
mylist = list("ABCDEFGH")

# Choose a single random element from the list
a = random.choice(mylist)
print(a)

# Choose 3 unique elements from the list
b = random.sample(mylist, 3)
print(b)

# Choose 3 elements from the list with replacement (can repeat)
c = random.choices(mylist, k=3)
print(c)

# Shuffle the list in place (modifies the list)
random.shuffle(mylist)
print(mylist)

# Set a seed to make the random numbers predictable (useful for debugging)
random.seed(1)
print(random.random())          # This will always print the same number for the same seed
print(random.randint(1, 10))    # Same here

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# Resetting the seed to same values will generate same numbers again
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# More secure random numbers using secrets module
import secrets

# Generate a random integer between 0 and 9 (10 not included)
a = secrets.randbelow(10)
print(a)

# Generate a random integer with 4 random bits (range: 0 to 15)
b = secrets.randbits(4)
print(b)

mylist = list("ABCDEFGH")

# Choose one element securely from the list
c = secrets.choice(mylist)
print(c)

# Using numpy for random operations
import numpy as np

# Generate a 1D array with 3 random float numbers between 0 and 1
a = np.random.rand(3)
print(a)

# Generate a 2D array (3x3) of random float numbers
b = np.random.rand(3, 3)
print(b)

# Generate a 1D array of 3 random integers between 0 and 9
c = np.random.randint(0, 10, 3)
print(c)

# Generate a 2D array (3x4) of random integers between 0 and 9
c = np.random.randint(0, 10, (3, 4))
print(c)

# Create a 2D numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# Shuffle the rows of the array (in-place)
np.random.shuffle(arr)
print(arr)

# Set seed for reproducibility in numpy
np.random.seed(1)
print(np.random.rand(3, 3))

# Reset seed and regenerate to get the same result
np.random.seed(1)
print(np.random.rand(3, 3))
