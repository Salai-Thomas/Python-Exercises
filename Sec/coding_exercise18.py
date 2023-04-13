# Calculate the midpoint of the segment with ends at the points: A = (2, 4), B = (-4, 6) and print result to the console as shown below.

# Expected result:

# The middle point: (-1.0, 5.0)

##My comments

# A = (x1,y1)
# B = (x2,y2)

#mid point = (x1+x2/2,y1+y2/2)

A = (2, 4)
B = (-4, 6)

x1 = 2
y1 = 4
x2 = -4
y2 = 6
mid_point = ((x1+x2)/2,(y1+y2)/2)

print(f'The middle point: {mid_point}')