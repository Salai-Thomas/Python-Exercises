# Implement the sort_list() function that sorts a list of two-element tuple objects according to the second element of the tuple.



# Example:



# [IN]: sort_list([(1, 3), (4, 1), (4, 2), (0, 7)])
# [OUT]: [(4, 1), (4, 2), (1, 3), (0, 7)]


# [IN]: sort_list([('a', 'b'), ('g', 'a'), ('z', 'd')])
# [OUT]: [('g', 'a'), ('a', 'b'), ('z', 'd')]


# Tip: Use the sorted() function.
# Note! You only need to define the function.

def sort_list(lst):
     print(sorted(lst, key=lambda x: x[1]))

sort_list([(1, 3), (4, 1), (4, 2), (0, 7)])
sort_list([('a', 'b'), ('g', 'a'), ('z', 'd')])
