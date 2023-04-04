# An infinite geometric sequence is given with the following formula:

# 1,1/2,1/4,1/8...
# Calculate the sum of this sequence. Print the result to the console as shown below.

# Expected result:
# The sum of the sequence: 2.0
import math
sequence = [1,1/2,1/4,1/8]
sumResult = math.ceil(sum(sequence))

print(f'The sum of the sequence: {sumResult}')