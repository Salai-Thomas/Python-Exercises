# The following tuple is given:

# techs = ('python', 'java', 'sql', 'aws')

# Sort this tuple from a to z and print it to the console.

# Tip: Tuples are immutable. You have to create a new one.

# Expected result:

# ('aws', 'java', 'python', 'sql')

techs = ('python', 'java', 'sql', 'aws')
sorted_tup = sorted(techs)

print(tuple(sorted_tup))