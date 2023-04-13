# Calculate the distance of two points A = (3, 2), B = (- 1, -1) and print result to the console as shown below.

# Expected result:

# The distance between points A and B: 5.0

## My comments

# distance = sqrt((x2-x1)**2 + (y2-y1)**2)

import math

A = (3, 2)
B = (- 1, -1)

x1,y1 = A
x2,y2 = B

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f'The distance between points A and B: {distance}')