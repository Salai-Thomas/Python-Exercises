# Greatest Common Divisor (GCD) of two integers - this is the largest natural number that divides both of these numbers without a remainder.

# For example, for numbers 32 and 48, the greatest common divisor is 16, which we can write GCD(32, 48) = 16.

# Implement a function called greatest_common_divisor() that determines the greatest common divisor of two numbers.

# Example:

# [IN]: greatest_common_divisor(32, 48)

# [OUT]: 16

# You just need to implement the function. The  tests run several test cases to validate the solution.

def greatest_common_divisor(n1, n2):
    if n1 < n2:
        x = n1 // 2
    else:
        x = n2 // 2

    if n1 % x == 0 and n2 % x == 0:
        print(x)

greatest_common_divisor(32,48)