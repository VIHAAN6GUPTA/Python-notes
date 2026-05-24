# Importing the sys module to access command-line arguments
import sys

# Getting the first argument passed from the command line (after the script name)
# Example: if run as `python script.py Mike`, then name will be "Mike"
name = sys.argv[1]

# Print a greeting using the name from command-line
print("Hello " + name)

# Importing argparse module to handle command-line options and arguments in a more powerful way
import argparse

# Creating an ArgumentParser object with a description shown when using --help
parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

# Adding a required argument (flag: -c or --color)
# - 'metavar' is just the name shown in the help message
# - 'required=True' makes this argument mandatory
# - 'choices' restricts input to only 'red' or 'yellow'
# - 'help' provides a description shown in --help
parser.add_argument(
    '-c', '--color',
    metavar='color',
    required=True,
    choices={'red', 'yellow'},
    help='the color to search for'
)

# Parse the command-line arguments provided by the user
args = parser.parse_args()

# Print the selected color from the command-line input
print(args.color)


# How to run this code in terminal

#python accepting_arguments.py Mike -c red

# Output

#Hello Mike
#red

# Function that accepts positional, variable positional (*args), and variable keyword arguments (**kwargs)
def func(a, b, *args, **kwargs):
    print(a, b)  # Print first two positional arguments
    for arg in args:
        print(arg)  # Print all additional positional arguments
    for key in kwargs:
        print(key, kwargs[key])  # Print keyword argument key and its value (Corrected from kwargs(key) to kwargs[key])

# Calling the function with 2 positional, 3 *args, and 2 **kwargs
func(1, 2, 3, 4, 5, six=6, seven=7)

# Function with mandatory keyword-only arguments (after *) 
def func2(a, b, *, c, d):
    print(a, b, c, d)  # All arguments are printed; c and d must be passed as keyword arguments

# Valid call with keyword-only arguments c and d
func2(1, 2, c=3, d=4)

# Function that takes exactly 3 positional arguments
def func3(a, b, c):
    print(a, b, c)

# Unpacking list elements as positional arguments
my_list = [0, 1, 2]
func3(*my_list)

# Unpacking dictionary items as keyword arguments
my_dict = {'a': 1, 'b': 2, 'c': 3}
func3(**my_dict)

# Function that modifies a mutable list passed to it
def func4(a_list):
    a_list.append(4)       # Adds 4 to the end of the list
    a_list[0] = 100        # Changes the first element to 100

# Original list
my_list = [1, 2, 3]
func4(my_list)
print(my_list)  # List is modified in place: [100, 2, 3, 4]
