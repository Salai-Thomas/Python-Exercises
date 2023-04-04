# Write a program that compares two lists and returns True if the lists contain at least one of the same element. Otherwise, it will return False.

# Use break statement in the solution and print result to the console.

# Lists:

# list1 = [1, 2, 0]
# list2 = [4, 5, 6, 1]

# Expected result:

# True

lst1 = [1, 2, 0]
lst2 = [4, 5, 6, 1]

for x in lst1:
    for y in lst2:
        if x == y:
            print(True)
            break
    else:
        continue
    break
else:
    print(False)