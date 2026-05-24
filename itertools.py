# Itertools: Useful functions for efficient looping

from itertools import product  # Cartesian product
a = [1, 2]
b = [3, 4]
# Creates all possible pairs (a, b) where a is from first list and b from second
print(list(product(a, b)))     # [(1, 3), (1, 4), (2, 3), (2, 4)]

from itertools import permutations  # All possible orderings
a = [1, 2, 3]
# All 2-length permutations of the list elements
print(list(permutations(a, 2)))     # [(1, 2), (1, 3), (2, 1), ..., (3, 2)]

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
# All 2-length combinations (no repetition, order doesn't matter)
print(list(combinations(a, 2)))              # [(1, 2), (1, 3), ..., (3, 4)]
# All 2-length combinations with replacement (elements can repeat)
print(list(combinations_with_replacement(a, 2)))  # [(1, 1), (1, 2), ..., (4, 4)]

from itertools import accumulate
import operator
a = [1, 2, 6, 3, 4, 5]
# Running sum of the list
print(list(accumulate(a)))                   # [1, 3, 9, 12, 16, 21]
# Running maximum of the list
print(list(accumulate(a, func=max)))         # [1, 2, 6, 6, 6, 6]
# Running multiplication of elements (factorial-like)
print(list(accumulate(a, func=operator.mul)))  # [1, 2, 12, 36, 144, 720]

from itertools import groupby
a = [1, 2, 3, 4, 5, 6]
# Function to group elements by whether they are smaller than 3
def smaller_than_3(x):
    return x < 3

# Group elements based on the key function (returns a key and a group)
group_object = groupby(a, key=smaller_than_3)
for key, value in group_object:
    print(key, list(value))   # True: [1, 2], False: [3, 4, 5, 6]

# Grouping list of dicts by age
persons = [
    {'name': 'Tim', 'age': 25}, 
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27}, 
    {'name': 'Claire', 'age': 28}
]

# Note: groupby requires the list to be sorted by the key
group_object1 = groupby(persons, key=lambda x: x['age'])
for key, value in group_object1:
    print(key, list(value))   # Groups persons with same age

from itertools import count, cycle, repeat

# count(start): generates an infinite sequence starting from 'start'
for i in count(10):
    print(i)
    if i == 15:               # Stop after 15 to avoid infinite loop
        break

a = [1, 2, 3]
# cycle(a): infinitely repeats the list
counter = 0
for i in cycle(a):
    print(i)
    counter += 1
    if counter == len(a):    # Stop after one full cycle
        break

# repeat(element, times): repeats an element 'times' number of times
for i in repeat(1, 4):
    print(i)  # Prints 1 four times
