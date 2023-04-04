# The following list is given:

# characters = ['k', 'b', 'c', 'j', 'z', 'w']

# Using the built-in functions, return the first and the last letter in alphabetical order from this list and print the result to the console as shown below.

# Tip: Use the min() and max() functions.

# Expected result:

# First: b
# Last: z

characters = ['k', 'b', 'c', 'j', 'z', 'w']

first = min(characters)
last = max(characters)

print(f'First: {first}')
print(f'Last : {last}')
