# The following dictionary:

# stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

# save to stocks.json using the json package. Set the indent to 4.

# File stocks.json after saving:

# {
#     "PLW": [
#         "Playway",
#         350
#     ],
#     "BBT": [
#         "Boombit",
#         22
#     ]
# }

import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json','w')as f:
    json.dump(stocks,f,indent=4)