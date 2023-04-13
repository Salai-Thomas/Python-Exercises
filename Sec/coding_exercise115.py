# The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

# with open('playway.csv', 'r') as file:
#     content = file.read().splitlines()

# Find the day with the highest volume value for the given month and print the result to the console as shown below.

# Expected result:

# Date: 2020-03-13

with open('playway.csv','r')as file:
    content = file.read().splitlines()
    extract_col = content[1:]
    spl = []
    vol = []
    date = []

    for index,value in enumerate(extract_col):
        spl.append(extract_col[index].split(','))
    
    for index,value in enumerate(spl):
        vol.append(spl[index][5])
        date.append(spl[index][0])
    
    rm_col = [int(x.replace("'",'')) for x in vol]

    max_indx = rm_col.index(max(rm_col))

    max_date = date[max_indx].replace("'",'')

    print("Date: ",max_date)
    