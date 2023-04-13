# All natural numbers divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15]. The sum of these numbers is: 51. In this exercise, we treat zero as a natural number.

# Find the sum of all numbers that are divisible by 5 or 7 less than 100.

# Present the solution in the form of a function called calculate(). In response, call calculate() function and print the result to the console.

# Expected result:

# 1580

def calculate(num1,num2):
    lst = [x for x in range(100) if x % num1 == 0 or x % num2 == 0 ]
    print(sum(lst))

calculate(5,7)


