import time
import os
import math
import csv 
import sys

# #print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
# #print(os.getcwd())

# f = open('portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# for row in rows:
#     print(row)


def portfolio_cost(filename):
    
    
    
        
    f = open('portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0.0
    for row in rows:
        try:
            nshares = int(row[1])
        except ValueError:
            print("couldn't parse", rows)
            continue
        try:
            price = float(row[2])
        except ValueError:
            print("couldn't parse", rows)
            continue
        total_cost += nshares * price
        print("The cost per company's shares is, ", round((nshares*price),2), ' and the total cost is ', round(total_cost, 2), end=time.sleep(0.5))
        #print('Total cost', total_cost)
    return total_cost
    f.close()

if len(sys.argv) == 2:
    filename = sys.argv[1]
else: 
    filename = ''r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data\portfolio.csv'''

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost, end=time.sleep(1))