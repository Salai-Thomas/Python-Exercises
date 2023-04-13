# The arithmetic sequence is given with the following formula:

# Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.
# an = 10 + 4n
# Expected result:

# The sum of the first 10 elements in a sequence: 320.0

# a_1 = 14 (my comment)
# a_10 = 50

# (sum of the first term formula) Sn=n(a1 + an)/2 (my comment)

# an = 10 + 4n

a1 = 10 + 4*1
a10 = 10 + 4*10
n = 10  
an = 10 + 4*n
s_n = n*(a1 + an)/2

print(f'The sum of the first 10 elements in a sequence: {s_n}')
