# names = ['Elwood', 'Jake', 'Curtis']
# nums = [ 39, 38, 42, 65, 111]


# line = 'GOOG,100,490.10'
# row = line.split(',')

# #print(row)

# names.append('Murphy')

# #print(names)

# names.insert(2, 'Arethra')

# #print(names)



# # s = [1,2,3]
# # t=['a','b']
# # d = s + t
# # print(d)



# # print(names)
# # print(names[0])
# # print(names[1])
# # print(names[2])
# # print(names[3])
# # print(names[4])

# #print(names[-2])


# # names[1] = 'Joliet Jake'

# # print(names)


# # print('Elwood' in names)

# # print('Britney' in names)


# # s = [1,2,3]

# # s * 3

# # print(s)



# # for name in names:
# #     print(names[0] + ' ' + names[3])

# # print(names.index('Curtis'))


# # x = names.remove('Curtis')
# # print(names)

# # y = names.append('Curtis')
# # print(names)

# # names.sort()  #sorts list in place but does not return a sorted list. must print or return the list to see it
# # print(names)


# # print(sorted(names))

# # Lists were not designed for math

# # print(nums*2)
# # print(nums + [1] + [2] +[4])



# symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
# symlist = symbols.split(',')
# #print(symlist)
# #print(symlist[0])
# #print(symlist[2])
# #print(symlist[5])

# symlist[2] = 'AIG'
# #print(symlist)

# #print(symlist[0:3])
# #print(symlist[-2:])

# mysyms = []
# mysyms.append('GOOG')
# #print(mysyms)

# symlist[-2:] = mysyms
# #print(symlist)

# for s in symlist:
#     print('s = ', s)

# x = 'AIG' in symlist
# y = 'AA' in symlist
# z = 'Cat' not in symlist
# print(x,y,z)



# symlist.append('RHT')
# print(symlist)

# print(symlist)

# symlist.insert(2, 'AA')

# print(symlist)

# symlist.remove('MSFT')
# symlist.sort()
# print(symlist)

# x = symlist.index('YHOO')
# print(x)

# y = symlist.remove('YHOO')
# print(symlist)

# symlist.sort(reverse=True)
# print(symlist)

# a = ','.join(symlist)
# print(a)
# b =':'.join(symlist)
# print(b)
# c = ''.join(symlist)
# print(c)

# nums = [1,2,3,4,5]
# letters = ['a','b','c','d','e', nums]
# items = ['hello', 'mello', 'jello', 'yellow', nums, letters]
# # print(items)

# #use multiple index searching to search for positions in nested lists

# print(items)


#insert syntax listname.insert(#, <insert value>)
#inserts can be nested as per below

items = [ 'GOOG', 'AAP', 'AAXX', 'WEED']
nums = [1,2,3,4,5]
forthelulz = ['spam', 'lol', 'mim', 'kij']
MOARnumbers = [56,76,78,23436]

list = []

list.insert(0, items)
#print(list)

list.append(nums)
#print(list)

list[0].append('hello')
#print(list)


list[0].remove('hello')
#print(list)

list[0].insert(0, 'hello')
#print(list)

list[0].remove('hello')
#print(list)

list[1].insert(0, 'hello')
#print(list)

list.append('')
#print(list)

tmp = list[1] #take list at position [1]
list[1] = list [1+1] #list at position[1] is now position 1 + 1 or position 2
list[1+1] = tmp #list at position [2] is now position [1]

#print(list)

list[1] = 'hello'
#print(list)

list.append(1)
#print(list)

list.insert(1, 'mullo')
#print(list)

list[0].insert(2, MOARnumbers) #inserts a list in a list
#print(list)

list[0][2].insert(0, forthelulz) #inserts a list in a list in a list
#print(list)

newlist = [2,2,2,2,2,2]
newishlist = [4,4,4,4]

list[0][2][0].insert(2, newlist)
#print(list)

list[0][2][0][2].insert(4, newishlist) #notice the patter of the index positions? for the index position added in the insert call simply gets added to the index positions on the list variable before the next insert function is called on it for the next list
print(list) #this may not be the best pythonic design and could get very clunky very quickly - use with caution