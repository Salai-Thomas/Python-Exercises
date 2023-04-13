# The geometric sequence is given with the following formula:

# Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.

# an = 8.2 n-1
# Expected result:

# The sum of the first 6 elements of the sequence is: 504.0

#  Sn=a(1-rn)/r-1 sum geometric sequence formula (my comment)
# an = r n-1 (my comment)
# r  = 8.2 (my comment)

a1 = 1
r = 8.2
n = 6

s_6 = a1*(1 - 8.2**6)/(1-8.2)

print(f'The sum of the first 6 elements of the sequence is: {s_6}')

