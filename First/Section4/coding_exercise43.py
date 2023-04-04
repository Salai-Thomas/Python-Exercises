# The following text is given:

# text = """Python is a general-purpose language.
# Python is popular."""

# Using the appropriate method, split the text into sentences. Print the result as a list to the console.

# Expected result:

# ['Python is a general-purpose language.', 'Python is popular.']

text = """Python is a general-purpose language.
# Python is popular."""

spl=text.split("#")
lst1= spl[0].strip()
lst2= spl[1]
new_list =[lst1,lst2]

print(new_list)

# if '\n'in spl[0]:
#     print()
