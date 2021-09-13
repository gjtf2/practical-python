# pcost.py

import time
import os
import math

#print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
#print(os.getcwd())

total_cost = 0.0

with open('portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price
        #print("The cost per company's shares is, ", round((nshares*price),2), ' and the total cost is ', round(total_cost, 2), end=time.sleep(0.5))

print('Total cost', total_cost)