# Implement a function called maximum() that returns the maximum of three numbers. Use conditional statement.

# Example:

# [IN]: maximum(4, 2, 1)
# [OUT]: 4

# [IN]: maximum(-3, 2, 5)
# [OUT]: 5

# Note! You only need to define the function.

def maximum(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

maximum(4, 2, 1)
maximum(-3, 2, 5)
