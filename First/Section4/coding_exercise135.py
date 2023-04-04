# Implement a function is_distinct() to check if the list contains unique values.



# Example:



# [IN]: is_distinct([1, 2, 3])
# [OUT]: True


# [IN]: is_distinct([1, 2, 3, 3])
# [OUT]: False


# Note! You only need to define the function.

# def is_distinct(lst):
#     print(len(set(lst)) == len(lst)) 

# is_distinct([1, 2, 3])
# is_distinct([1, 2, 3, 3])

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6)

