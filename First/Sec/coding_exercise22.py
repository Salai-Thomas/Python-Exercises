# An infinite geometric sequence is given with the following formula:

# 1,1/2,1/4,1/8,...

# Calculate the sum of this sequence. Print the result to the console as shown below.

# Expected result:

# The sum of the sequence: 2.0

## My comments

#  s = a/(1-r)# sum infinite geometric sequence formula

a = 1 #first term
r = 1/2 # common ration

sum_sequence = a/(1-r)

print(f'The sum of the sequence: {sum_sequence}')