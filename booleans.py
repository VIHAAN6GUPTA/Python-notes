# Initially assigned a boolean value
done = True

# Then reassigned to a string
done = "Mike"

# Then reassigned to an integer
done = 1

# Then reassigned to an empty string
done = ""

# Check if the type of 'done' is boolean
print(type(done) == bool)  # False, because 'done' is now a string ("")

# Check the truthiness of 'done'
if done:
    print("yes")
else:
    print("no")  # Output will be "no" because an empty string is considered False

# Boolean values indicating whether each book was read
book1_read = True
book2_read = False

# Check if any book has been read (True if at least one is True)
read_any_book = any([book1_read, book2_read])
print(read_any_book)  # Output: True

# Check if all books have been read (True only if all are True)
read_any_book = all([book1_read, book2_read])
print(read_any_book)  # Output: False
   