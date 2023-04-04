# The following text is given:

# text = 'Programming in python.'

# Follow the next steps:

# Change all letters to lowercase.

# Delete spaces and period.

# Create a set consisting of all letters in the text and assign to letters variable

# Using the appropriate method for sets, remove all vowels from letters set:

# vowels = {'a', 'e', 'i', 'o', 'u'}
 
# 5. Print the number of items in the letters set as shown below.

# Expected result:

# Number of items: 8

text = 'Programming in python.'
l_text =text.lower()
sp_rm = l_text.replace(' ','')
letters = set(sp_rm.replace('.',''))
vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    if vowel in letters:
        letters.discard(vowel)
    else:
        print("false")

print(len(letters))
print(f'Number of items: {letters}')