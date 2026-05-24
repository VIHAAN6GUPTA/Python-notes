import math  # from math import sqrt

print(math.sqrt(4))

print(abs(-5.5))         # Output: 5.5
print(round(5.4))        # Output: 5
print(round(5.498, 1))   # Output: 5.5

from enum import Enum

# Define an enumeration
class State(Enum):
    INACTIVE = 0
    ACTIVE = 2

# Access enum member by name (as a string key)
print(State['ACTIVE'])        # Output: State.ACTIVE

# Access value of enum member
print(State.ACTIVE.value)     # Output: 2


# List all members of the enum
print(list(State))            # Output: [<State.INACTIVE: 0>, <State.ACTIVE: 2>]
