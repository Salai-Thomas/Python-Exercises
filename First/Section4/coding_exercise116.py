# Generate all even numbers from 2 to 18 inclusive. Then write each number on a separate line to the file called num.txt.

# File num.txt after saving:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

with open('num.txt', 'w') as file:
    for i in range(2, 19, 2):
        file.write(str(i) + '\n')

