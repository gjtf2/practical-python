billHeight = 0.11 * 0.001 # the thickness of a single bill
towerHeight = 442
numBills = 1 
numDays = 1

# numBillsInHeight = towerHeight / billHeight
# print(numBillsInHeight)


while numBills * billHeight < towerHeight:
    print(numDays, numBills, numBills * billHeight)
    numDays = numDays + 1
    numBills = numBills * 2
    

print('Number of Days', numDays)
print('Number of bills', numBills)
print('Final Height', numBills * billHeight)
