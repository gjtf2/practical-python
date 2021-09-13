# #f = open('foo.txt', 'rt') #open for reading
# g = open('bar.txt', 'w+') #open for writing

# g.write('write some text')

# for i in range(10):
#     g.write('hello my mellow yellow')

# g.close()

# f = open('bar.txt', 'r+')

# f.truncate(0)
# f.close()

# f = open('bar.txt', 'w+')

# for i in range(10):
#     f.write('\nhello')

    

# with open('bar.txt', 'w+') as file:
#     for i in range(10):
#         file.write('\nbaby back ribs')

# with open('bar.txt', 'rt') as file:
#     data = file.read()

# print(data)

# with open('bar.txt', 'a') as file:   #this is the append function so as to not overwrite existing contents in a file!!! neat!
#     for i in range(10):
#         file.write('\nare delicious')

# with open('bar.txt', 'rt') as file:
#     data = file.read()

# print(data)

# with open('bar.txt', 'w+') as file:
#     file.truncate(0)
#     x = file.read()
#     print(x)


# with open('bar.txt', 'w+') as file:
#     for i in range(10):
#         file.write('\nbaby back ribs')
        

# with open('bar.txt', 'rt') as filez:
#     data = filez.read()
#     #print(data)

# with open('bar.txt', 'r+') as file:
#     for line in file:
#         for i in range(10):
#             file.write('\n are delicious')



# with open('bar.txt', 'w+') as file:
#     file.truncate(0)

# with open('bar.txt', 'wt') as out:
#     out.write('Hello world\n')

# with open('bar.txt', 'wt') as out:
#     print('Hello World', file=out)


# import os

# print(os.getcwd())
# os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
# print(os.getcwd())

# with open('portfolio.csv', 'rt') as f:
#     data = f.read()

# print(data)


import os
print(os.getcwd())
os.chdir(r'C:\Users\gjtf2\Documents\GitHub\practical-python\Work\Data')
print(os.getcwd())

# import time

# with open('portfolio.csv', 'rt') as f:
#     for line in f:
#         print(line, end=time.sleep(0.5))  #import time and specify a number of seconds to display the line)

# import time
# f = open('portfolio.csv','rt')
# headers = next(f) #next returns the next text line in a file (that contains text)
# #print(headers)
# for line in f:
#     print(line, end=time.sleep(0.4))

# f.close()

# import time
# f = open('portfolio.csv',  'rt') 
# headers = next(f).split(',')
# print(headers)
# for line in f:
#     row = line.split(',')
#     print(row, end=time.sleep(0.5))

# f.close()






