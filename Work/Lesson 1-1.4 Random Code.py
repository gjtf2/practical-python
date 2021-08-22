# Single Quote

#a = "yeah but no but yeah but"

# Double Quotes

#b = "computer says no"

 # Triple Quotes

# c =  '''
# Look into my eyeskjbjdwbjkw
# bkfewhbifwbi
# jbfewbjifeboj
# lkbfbqfql'''


# '\n'      Line feed
# '\r'      Carriage return
# '\t'      Tab
# '\''      Literal single quote
# '\"'      Literal double quote
# '\\'      Literal backslash


# a = '\xf1'          # a = 'ñ'
# b = '\u2200'        # b = '∀'
# c = '\U0001D122'    # c = '𝄢'
# d = '\N{FOR ALL}'   # d = '∀'

# print('\n   ', a, '\n  ', b, '\n ', c, '\n', d)
# print(a,b,c,d)

# a='Hello World'
# b = a[1]
# c = a[2] #square brackets with a single integer ID a position relative to the string
# d = a[3:8] #square brackets with an int:int or int: ID a 'slice' of the string
# e = a[4:] #a slice that continues to the end of the string starting from the relative position identified by the integer on the left side of the colon
# f = a[-5] # a relative position where the minus finds the position of the interger from the end of the input string 
# print(b,c,'\n', d, '\n', e, '\n', f)


# concatenation

# a = 'hello world'
# b = 'Say ' + a
# c = 'Say ' + '"' + a + '"' 
# print(b,'\r',c)

# # Length

#s = '           hel   lo worlds   '
# print(len(s))


# membership test

# t = 'e' in s
# f = 'x' in s
# g = 'hi' in s
# h = 'hi' not in s
# o = 'e' in s[5]

# print(t,f,g,h, '\n', o)

#replication

# rep = s * 5
# rep1 = (s + ' ') * 5
# rep2 = ('\n' 'Say ' +  s + '  ') * 5
# print(rep,rep1,rep2)

#stripping

# t = s.strip()  #strip() only strips whitespace at the beginning or end of a string, not in the middle
# print(t)


# case conversion

# a = 'Hello'
# b = a.lower()
# c = a.upper()
# print('The original string is ' + a, '\n', 'The string with lower() is, ' +  b, '\n', 'The string with the upper() is, ' + c)


# Replacing Text in a string

# a = 'You motherfucking dog!'
# b = a.replace('fucking', 'ducking') #the first string is the original to be replaced and the second string is the replacement text)
# print(b)

# s.endswith(suffix)     # Check if string ends with suffix
# s.find(t)              # First occurrence of t in s
# s.index(t)             # First occurrence of t in s
# s.isalpha()            # Check if characters are alphabetic
# s.isdigit()            # Check if characters are numeric
# s.islower()            # Check if characters are lower-case
# s.isupper()            # Check if characters are upper-case
# s.join(slist)          # Join a list of strings using s as delimiter
# s.lower()              # Convert to lower case
# s.replace(old,new)     # Replace text
# s.rfind(t)             # Search for t from end of string
# s.rindex(t)            # Search for t from end of string
# s.split([delim])       # Split string into list of substrings
# s.startswith(prefix)   # Check if string starts with prefix
# s.strip()              # Strip leading/trailing space
# s.upper()              # Convert to upper case

# s = 'the quick brown fox jumps over the lazy dog'
# a = s.endswith('es') #boolean
# b = s.find('h') # integer
# c = s.index('h') #integer
# d = s.split('quick')
# print(a,b,c,d)

#string conversion

# x = 42
# print(str(x))

# byte strings

# data = b'Hello World\r\n'
# a = len(data)
# b = data[0:5]
# c = data.replace(b'Hello', b'Cruel')
# #print('The original data is, ' + str(data), '\n', a, '\n',b, '\n', c)

# #print(data[0])

# text = data.decode('utf-8')
# data2 = text.encode('utf-8')

# print('This is data decoded, ' + str(text), '\n', 'This is data encoded, ' + str(data2))


# F-Strings

name = 'IBM'
shares = 100
price = 91.1
a = f'{name:>10s}{shares:10d}{price:10.2f}'
print(a)

b = f'Cost = ${shares*price:0.2f}'
print(b)



