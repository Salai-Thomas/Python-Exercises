# The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

# with open('playway.csv', 'r') as file:
#     content = file.read().splitlines()

# Find the highest volume for a given month and print the result to the console as shown below.

# Expected result:

# Max Vol: 100412

with open('playway.csv','r') as file:
    content = file.read().splitlines()
    extract_1 =content[1:]
 
    volume_lst = []
    lst = []
    lst_2 = []

    for index,value in enumerate(extract_1):
        volume_lst.append(extract_1[index])

    for index,vlaue in enumerate(volume_lst):
        lst.append(volume_lst[index])
    
    for index,value in enumerate(lst):
        lst_2.append(lst[index].split(',')[5])
    
    lst_3 = [int(x.replace("'",'')) for x in lst_2]
    print('Max Vol: ',max(lst_3))
        

        
    
  