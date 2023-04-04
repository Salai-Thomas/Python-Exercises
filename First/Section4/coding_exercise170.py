# The following list is given:

# indexes = ['WIG20', 'mWIG40', 'sWIG80']

# Using dict comprehension, convert the above list into the following dictionary:

# {0: 'WIG20', 1: 'mWIG40', 2: 'sWIG80'}

# Print the result to the console.

indexes = ['WIG20', 'mWIG40', 'sWIG80']
dct = {x:y for x,y in enumerate(indexes)}

print(dct)