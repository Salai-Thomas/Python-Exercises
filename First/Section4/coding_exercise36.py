# The following codes are given:

# code1 = 'FVNISJND-20'
# code2 = 'FVNISJND20'

# Using the appropriate method, check whether the codes consist only of alphanumeric characters (numbers + letters). Print the result to the console as shown below.

# Expected result:

# code1: False
# code2: True

code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

check_c1 = code1.isalnum()
check_c2 = code2.isalnum()

print(f"code1: {check_c1}")
print(f"code2: {check_c2}")