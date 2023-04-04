# Write a program that prints to the console the first ten prime numbers separated by a comma.

# Tip: Use a while loop with break statement.

# Expected result:

# 2,3,5,7,11,13,17,19,23,29

num = 2  
count = 0 

while count < 10:

    for i in range(2, num):
        if num % i == 0:          
            break
    else:
        print(num, end=", ")
        count += 1
    num += 1


