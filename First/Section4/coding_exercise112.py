# Read the currencies.txt file. Each line has a different currency pair. Create a list with the names of currency pairs containing the 'USD' symbol.

# Expected result:

# ['ARSUSD', 'AUDUSD']


with open('currencies.txt', 'r') as file:
    lines = file.readlines()

usd_pairs = []

for pair in lines:
    if 'USD' in pair:
        usd_pairs.append(pair.strip())  

print(usd_pairs)
