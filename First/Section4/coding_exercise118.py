# Two following lists are given:

# headers = ['user_id', 'amount']
# users = [['001', '1400'], ['004', '1300'], ['007', '900']]

# Save the above data to the users.csv file (file in csv format - comma-separated values) as shown below.

# File users.csv after saving:

# user_id,amount
# 001,1400
# 004,1300
# 007,900

import csv

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(users)
