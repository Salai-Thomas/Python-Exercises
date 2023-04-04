# Implement a function count_str(), which returns the number of str objects with a length more than 2 characters from an iterable object (list, tuple, set).

# Example:

# [IN]: count_str([1, '#hello', '', 'python', 'go'])
# [OUT]: 2

# [IN]: count_str([1, 2, 3, 'python'])
# [OUT]: 1

# Note! You only need to define the function.

def count_str(datas):
    count = 0
    for item in datas:
        if isinstance(item, str) and len(item) > 2:
            count += 1
    print(count)

count_str([1, '#hello', '', 'python', 'go'])
count_str([1, 2, 3, 'python'])
