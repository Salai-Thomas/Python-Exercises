# Calculate the standard deviation of the following set of data: 10, 11, 9.

# Print the result to the console as shown below.

# Expected result:

# The standard deviation: 0.82


## My Comments

#SD= √∑∣x−μ∣ ^2 /N //formula

# Step 1: Find the mean.
# Step 2: For each data point, find the square of its distance to the mean.
# Step 3: Sum the values from Step 2.
# Step 4: Divide by the number of data points.
# Step 5: Take the square root.

# set of data: 10, 11, 9

# μ(mean) = sum of the terms / number of the terms (step 1)

import math 

num_terms = 3
mean = (10 + 11 + 9 ) / num_terms

# ∣x−μ∣^2 # square of its distance to the mean (step 2)

x1 = (10- mean)**2
x2 = (11 - mean)**2
x3 = (9 - mean)**2

# Step 3: Sum the values from Step 2.
sum_xterm = x1+x2+x3

# Step 4: Divide by the number of data points.

result = math.sqrt(sum_xterm / num_terms)

print(round(result,2))

