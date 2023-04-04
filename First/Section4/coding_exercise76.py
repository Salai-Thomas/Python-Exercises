# The following dictionary is given:

# project_ids = {
#     '01': 'open', 
#     '03': 'in progress',
#     '05': 'in progress',
#     '04': 'completed'
# }

# Extract a list of unique values (sorted alphabetically) from the project_ids dictionary and print it to the console.

# Expected result:

# ['completed', 'in progress', 'open']


project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

lst = set([project_ids[i] for i in project_ids])
new_lst =sorted(lst)
print(new_lst)