# Implement a function count_str(), which returns the number of str objects in an iterable object (list, tuple, set).

# Example:

# [IN]: count_str(['p', 2, 4.3, None])
# [OUT]: 1

# [IN]: count_str({'p', 2, 4.3, True, 'True', None})
# [OUT]: 2

# Note! You only need to define the function.

def count_str(datas):
    count = 0
    for item in datas:
        if isinstance(item, str):
            count += 1
    print(count)

count_str(['p', 2, 4.3, None])
count_str({'p', 2, 4.3, True, 'True', None})
