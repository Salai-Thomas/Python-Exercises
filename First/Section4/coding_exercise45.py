# From the given url:

# url = (
#     'https://e-smartdata.teachable.com/'
#     'p/sciezka-data-scientist-machine-learning-engineer'
# )

# extract the slug after the last character '/'. Then replace all dashes with spaces and print the result to the console as shown below.

# Expected result:

# sciezka data scientist machine learning engineer

import re
url = (
    'https://e-smartdata.teachable.com/'
    'p/sciezka-data-scientist-machine-learning-engineer'
)

result = re.sub("(http|https)://\w\W[a-z]+\.[a-z]+\.[a-z]+/[a-z]/",' ',url)

rm_dash = result.replace('-',' ')

print(rm_dash)
