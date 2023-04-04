# Implement a generator named file_gen(), which selects only those names of files with the '.txt' extension from the list.



# Example:



# [IN]: fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
# [IN]: list(file_gen(fnames))
# [OUT]: ['data1.txt', 'data2.txt', 'data3.txt']


# Note! All you have to do is define a generator. 
fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
def file_gen(fnames):
    for name in fnames:
        if name.endswith('.txt'):
            yield name

list(file_gen(fnames))
