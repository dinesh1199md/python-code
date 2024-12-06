l=[1,2,3,4,5,6]
l.remove(6)
print(l.index(5)) #this will return the value of the indext
del l[0]
print(l)


def addtwolist(l1,l2):
    l3=list(l1+l2)
    l3.append([2,2,2])
    return l3
print(addtwolist([1,2,3,4],[5,6,7,8]))


#del and remove()
dellist=[1,2,43,4,6,7,8,9]

dellist.remove(43)
print(dellist)
dellist[3:]
print(":::::::::")
print(dellist)


from collections import Counter
def method3(array, k):
    counters = Counter(array)
    print(counters)
    return [count for count in counters if counters[count]>=k]

array = [1, 2, 2, 3, 3, 4]
print(method3(array, 2))




# def magic(a):
#     a=a*2
#     a=a+[4,5]
#     return a
# a=[1,2,3]
# print(magic(a))

# print(dir(int))


'''lru_cache'''
from functools import lru_cache
@lru_cache(maxsize=None)
def expensive_function(arg1, arg2):
    # Expensive computation
    pass


ele=[1,2,3,4,5,6,7,8]
print(sum([e for e in ele]))

''''remove duplicate'''
my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
seen=set()
uq=[]
dup=[]
for i in my_list:
    if i not in seen:
        uq.append(i)
        seen.add(i)
    else:
        dup.append(i)
print("hello this check")    
print(uq,dup,seen)        


'''intersection of list'''
def intersection_list(l1,l2):
     li=[]
     for i in l1:
         if i in l2:
             li.append(i)    
     return li
def method2(l1,l2):
    # Using set operations
    return list(set(list1) & set(list2))
def method_listcomp(l1,l2):
    # Using set operations
    return [i for i in l1 if i in l2]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# print(intersection_list(list1,list2))
# print(method2(list1,list2))
# print(method_listcomp(list1,list2))


''''types of square root'''
import cmath,math
def square_root(n):
    return n**0.5
def square_root_math(n):
    return math.sqrt(n)
def square_root_coplex(n):
    return cmath.sqrt(n)

# print(square_root(9))
# print(square_root_math(100))
# print(square_root_coplex(3+2j))


def swap_1at_2nd_value_list(l):
    l[-1],l[0]=l[0],l[-1]
    return l
# print(swap_1at_2nd_value_list([1,2,3,4,5,6]))


'''Combine the two lists below and discard identical values'''
a=[1,2,3,4,5]
b=[4,5,7,8,9]
common_values = set(a) & set(b) #get common values by using & symbol between two sets
joinlist = set(a+b) #Join two lists without duplicates by using set func
final_list = list(joinlist-common_values) #Remove identical values
print(common_values)
print(joinlist)
print(final_list) 