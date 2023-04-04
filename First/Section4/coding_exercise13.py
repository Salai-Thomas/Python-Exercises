# Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.

# Tip: Use compound capitalization of interest.

# Print the result to the console as shown below.

# Expected result:

# The future value of the investment: 1159.27 US

investValue = 1000
investRate = 3
years = 5
caculate = ((investValue/100)* investRate) * years
result = caculate + investValue

print(f"The future value of the investment: {result} US")
