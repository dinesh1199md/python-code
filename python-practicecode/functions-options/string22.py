

name="Dinesh"
rep="hey this is Dinesh, from Dinesh"

# print(name.capitalize())
# print(name.isalpha())
# print(name.isalnum())
# print(name.lower())
# print(name.upper())
# print(name.swapcase())
# print((name.rstrip()))
name.isalpha()

# print(rep.replace("Dinesh","Ganesh",1)) #replace(old str,New str,count)
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

'''Escape Sequences'''
a='''he\\llo\tthis i\ns 
Dine\'sh'''
print(a)

'''join() function merges elements of a list with some delimiter string, 
and returns the result as a string.
'''
#join function
list = ["One", "Two", "Three"]
print(",".join(list))
s=",".join(list)
print(type(s))

# Life cycle
''' string ->> split() ->> list[] ->> join() ->> string '''

'''plit() function splits the into tokens, based on 
some delimiters and returns the result as a list.'''

# split function
newList = s.split(',')
print(newList)
print(type(newList))