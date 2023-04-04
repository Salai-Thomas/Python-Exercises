# The following function is defined:

# def function(idx, l=[]):
#     for i in range(idx):
#         l.append(i ** 3)
#     print(l)

# Call the function three times as follows:

# function(3)
# function(5, ['a', 'b', 'c'])
# function(6)

# Analyze the results!

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6)