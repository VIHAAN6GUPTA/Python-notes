# Set a condition to True
condition = True

# While loop runs as long as the condition is True
while condition == True:
    print("The condition is true")
    # Set condition to False to stop the loop from repeating
    condition = False


# Initialize a counter variable
count = 0

# Loop while count is less than 10
while count < 10:
    print("The condition is true")
    # Increment count by 1 on each loop iteration
    count += 1

# This line executes after the above while loops are done
print("After the loop")


# Create a list with mixed elements
items = ["Roger", "Mike", 2, 3, 4]

# Iterate over each element in the list and print it
for item in items:
    print(item)


# Use enumerate to get both index and value during iteration
for index, item in enumerate(items):
    print(index, item)


# New list of numbers
items1 = [1, 2, 3, 4, 5]

# Loop through the list
for item1 in items1:
    if item1 == 2:
        # Skip printing this item and move to the next iteration
        continue 
    print(item1) 


# Loop through the list again
for item1 in items1:
    if item1 == 2:
        # Stop the loop entirely when item is 2
        break
    print(item1) 
