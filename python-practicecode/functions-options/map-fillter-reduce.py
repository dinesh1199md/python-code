''''The map() function iterates through all items in the given iterable and
executes the function we passed as an argument on each of them.'''

# syntax
# map(function,list)
def starwith(a):
    return a[0]=='A'
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starwith, fruit)
'''method 1'''
print(list(map_object))
# '''method 2'''
# for value in map_object:
#     print(value,end=", ")


# omap=list(map(lambda x:x[0]=='A',fruit))
# print(omap)


'''Similar to map(), filter() takes a function object and an iterable and creates a new list.

As the name suggests, filter() forms a new list that contains only elements that satisfy a 
certain condition, i.e. the function we passed returns True.

The syntax is:
filter(function, iterable(s))'''
def starwith(a):
    return a[0]=='A'

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = filter(starwith, fruit)
'''method 1'''
print(list(map_object))
filter_object = filter(lambda s: s[0] == "A", fruit)


"""reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, 
it returns a single value.
Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:
reduce(function, sequence[, initial])"""

from functools import reduce
l=[1,2,3,4,5,6]
print((reduce(lambda x,y:x+y,l)))