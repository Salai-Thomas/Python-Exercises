# Implement a function called concat() that accepts two lists in the format given below:

# l1 = [[1], [2]]

# l2 = [[3], [4]]

# and returns:

# [[1, 3], [2, 4]]

# Note: You only need to implement this function.

l1 = [[1], [2]]
l2 = [[3], [4]]

def concat(l1, l2):
     print([[a[0], b[0]] for a, b in zip(l1, l2)])

concat(l1,l2)
