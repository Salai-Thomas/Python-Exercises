# From the following text:

# string = 'PKV-89415-PLN'

# extract the code containing the first three and last three characters. Print the result to the console.

# Expected result:

# PKVPLN

string = 'PKV-89415-PLN'
first_three = string[0:3]
last_three = string[-3:]

print(first_three+last_three)