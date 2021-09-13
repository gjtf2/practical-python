import time
import os
import math

print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
print(os.getcwd())

with open('portfolio.csv',  'rt') as f: #open the .csv file
    headers = next(f).split(',') # go to the file, go to the next line in the file (pass over the first), split the headers into a list separated by commas
    myList = []  #create a list out of the for loop to populate items from the iteration into to math on
    for line in f: #iterate through the file data
        row = line.split(',') #create a new variable for each line in the file and split it with a comma into a list
        nameComp = row[0] # the first item in the list is the name of the company
        #print(nameComp)
        shareInteger = float(row[1]) # the 2nd item in the list is the # of shares
        priceFloat = float(row[2]) # the 3rd item in the list is the price per share
        costPerComp = shareInteger * priceFloat # calculates the total cost of shares, at current share price with current number of shares set per company
        myList.append(float(f'{costPerComp:0.2f}')) #formats as string to round nicely and converts to float. adds the total cost of share purchase for each company to a list
        print('The total cost for ' f'{shareInteger}', 'shares of', f'{nameComp}', 'is,', f'{costPerComp:.2f}', end=time.sleep(1))
    print(myList) #checks the list
    print('the total cost for all the shares is, ', math.fsum(myList), end=time.sleep(1)) #sums the floats in the list. 


# import gzip
# import os
# import time


# print(os.getcwd())
# os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
# print(os.getcwd())

# with gzip.open('portfolio.csv.gz', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         print(line, end=time.sleep(0.8))