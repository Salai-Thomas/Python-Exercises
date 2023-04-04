# Implement a function called transfer_zeros() which takes the list as an argument and return list with all zeros at the end.

# Example:

# [IN]: transfer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2])
# [OUT]: [3, 4, 2, 5, 1, 6, 2, 0, 0]

# Note: You only need to implement this function.
zero_count = 0
lst_out = []
def transfrer_zeros(lst):
    for items in lst:
        lst_out.append(items)
        if items == 0:
            lst_out.remove(0)
            global zero_count
            zero_count += 1
        
    while zero_count > 0:
        lst_out.append(0)
        zero_count -=1

transfrer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2])
print(lst_out)
        