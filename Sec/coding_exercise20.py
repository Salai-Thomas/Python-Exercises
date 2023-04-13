# Find the roots of the quadratic equation:

#x^2+5x+4 =0

# Print the result to the console as shown below.

# Expected result:

# x1 = -4.0
# x2 = -1.0

## My Comments

# Roots of Quadratic Equation 
# x = (-b ± √ (b2 - 4ac) )/2a

#x^2+5x+4 =0

import math

a,b,c = 1,5,4

sq = math.sqrt(b**2 - 4*a*c)
x1 = (-b + sq) / (2*a)
x2 = (-b - sq) / (2*a)

print(f'x1 = {x1}')
print(f'x2 = {x2}')