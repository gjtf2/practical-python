import time
import os
import math

# #print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
# #print(os.getcwd())

def portfolio_cost(filename):
    
    
    with open('missing.csv', 'rt') as f:
        total_cost = 0.0
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                nshares = int(row[1])
            except ValueError:
                print("couldn't parse", line)
                continue
            try:
                price = float(row[2])
            except ValueError:
                print("couldn't parse", line)
                continue
            total_cost += nshares * price
            print("The cost per company's shares is, ", round((nshares*price),2), ' and the total cost is ', round(total_cost, 2), end=time.sleep(0.5))
            #print('Total cost', total_cost)
        return total_cost
            

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost, end=time.sleep(1))