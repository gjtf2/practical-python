
# import time

# def sumcount(n): #defines a function
#     total = 0 #set total to 0
#     while n > 0: #while loop. executes so long as a condition specified is true
#         total += n # adds the value of whatever n is to the total
#         n -= 1 # decrements the argument number passed by 1
#         print(total, n, end=time.sleep(0.055))
#     return total

# a = sumcount(100)



# a = 10
# a = a + 7.5
# print(a)

# a = 10
# a += 7.5
# print(a)

# b = 10
# b = b - 7.5
# print(b)

# b = 10
# b -= 7.5
# print(b)


# import math
# x = math.sqrt(10)
# print(round(x, 2))

# import webbrowser
# import urllib.request
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()

# webbrowser.open('http://www.python.org/')

# import os
# print(os.getcwd())
# os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
# print(os.getcwd())

# with open('portfolio.csv', 'rt') as f:
#     for line in f:
#         fields = line.split()
#         try:
#             shares = int(fields[1])
#         except ValueError:
#             print("couldn't parse", line)

#raise RuntimeError('what a kerfuffle')

# def greeting(name):
#     #issues a greeting
#     print('hello ', name)

# a = greeting('Henry')
# b = greeting('Fischer')
# c = greeting('lorilai')


import time
import os
import math

#print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
#print(os.getcwd())

def portfolio_cost(filename):
    
    total_cost = 0.0
    with open('portfolio.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
 
cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)



