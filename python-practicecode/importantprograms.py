
'''second largest number'''
# sort the list 
# l=[1,4,3,8,5,9,20]
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>=l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l[-2])  

# ------------------------------------------

'''dublicate in the list'''
# l2=[2,4,5,6,3,4,8,9,6,7,5]
# orl=[]
# dubl=[]
# for i in l2:
#     if i not in orl:
#         orl.append(i)
#     else:
#         dubl.append(i)    
# print(orl)     
# print(dubl)   

# --------------------------------------------------
'''Print The Repeate Number'''
# l=[1,2,3,4,4,5,6,7,6,10,10]
# k={}
# ### Print("------ Dinesh ------")
# for i in l:
#     if i in k:
#         k[i]=k[i]+1
#     else:
#         k[i]=1
# print(k)

# # ----------------------------------------------------

'''yield keyword,its return the generator object and convert a python function into the generator
 function '''
# def creating_gen(index):  
#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
#     yield (months[index])  
#     yield months[index+2]   
# next_month = creating_gen(3)  
# print(next(next_month), next(next_month))

# ##-----------------------------------------------------------

'''random module'''
# import random as ra
# l=[1,2,3,4,56,6,88,91]
# print(ra.random())
# print(ra.uniform(1,10))
# print(ra.randint(10,20))
# print(ra.randrange(10,80,3))

# print([ra.randint(0, 10) for i in range(5)])
# print([ra.randrange(0, 10,2) for i in range(5)])

'''to suffle the list'''
# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)


#--------------------------------------------------------------------
# # print(sum(range(1,102)))
'''glopal variable '''
# global_var = 100
# def modify_global_var():  
#     global global_var # Setting global_var as a global variable  
#     # global_var = 10  
#     print(global_var)
# def printing_global_var():  
#     print(global_var) # There is no need to declare global variable  
# modify_global_var()  
# printing_global_var() # Prints 10  

#-----------------------------------------------
'''mean number of list'''
# n=int(input("enter the mean number of elemet: "))
# l=[]
# for i in range(0,n):
#     k=int(input("enter the elemet: "))
#     l.append(k)
# mean= sum(l)/n
# print("mean",round(mean,2))

#------------------------------------
'''reverse simple'''
# l=[1,6,7,83,4,63,4]
# print(l[::-1])

'''reverse the numbers'''
# n=166229
# r=0
# while n>0:
#     digit=n%10
#     r=r*10+digit
#     n=n//10
# print(r) 

'''reverse the string'''
# name ="dineshmurugesan"
# number="753946"
# reverse=''
# for i in number:
#     reverse=i+reverse
# print(reverse)    

'''reverse the list'''
# l=[2,6,7,8,7,9,10]  

# # l=[1,2,3,4,5,6,7,8,9,10]
# left=0
# right=len(l)-1
# while left<right:
#     temp=l[left]
#     l[left]=l[right]
#     l[right]=temp
#     left+=1
#     right-=1
# print(l)    

#---------------------------------------------
''''dict features'''
# k={"k":1,"k1":4,"k2":6,"k3":4}
# print(k.get("k2"))
# print(k["k3"])

# # print(k.get("k4"))  #None
# # print(k["k4"])      #Key-error




'''merge dict work outs'''

k={"k":1,"k1":4,"k2":6,"k3":4}
k2={"l":11,"l3":14,"l4":9,"k3":4,"l1":1,"l2":5}

# final={}
# for key in k2.keys():
#     final[key]=k2[key]
# for key in k.keys():
#     final[key]=k[key]    

# for key in k:
#     for key2 in k2:
#         if key==key2:
#             final[key]=k[key]+k2[key2]
# print(final)

# print(k)
# print(k.pop("k3"))
# print(k)
# k["k3"]=44
# print(k.values())
# d2=dict(k.items())
# print(d2)

# for i,j in d2.items():
#     print(i,j,end=" ")


l=["a","b","c","d","e","f"]
def listtodict(l)->None:
    d={}
    for i,num in enumerate(l,0):
        d[i]=num
        print(f'{i}:{num}',end="\n")
    print(d)
def listtodict1(l)->dict:
    d={}
    for i,num in enumerate(l,0):
        d[i]=num
        # print(f'{i}:{num}',end="\n")
    return d    

from copy import deepcopy
def copyobj(l)->list:
    # l2=l.copy()
    l2=deepcopy(l)
    l[1][0]="Change"
    print(l)
    return l2

# print(listtodict(l))
# # print(listtodict1(l))
# l=["a",["d","def"],"c","d","e","f"]
# print(copyobj(l))




# n=(100000000)
# print(f'{n:,}')


'''automobile 2 and 4 wheeler '''

# tvehicle=int(input("Enter the TV: "))
# twheels=int(input("Enter the W: "))
# tvehicle=200
# twheels=540
# if (twheels>2) and (twheels%2)==0 and (tvehicle<twheels):
#     fwc=twheels-(2*tvehicle)
#     fw=fwc/2
#     twc=tvehicle-fw
#     print("two wheelers",twc)
#     print("four wheelers",fw)

# else:
#     print("pls checkes the inputs!!!")    

'''pattern print'''
# n=5
# num=1
# for i in range(1,n+1):
#     if i%2==0:
#         for j in range(n,0,-1):
#             print(num,end="  ")
#             num+=1
#             print()
#     else:
#         for j in range(n):
#             print(num,end="  ") 
#             num+=1  
#             print()

'''decatrator'''

# def lower_case(function):
#     def wrapper():
#         func=function()
#         lowercase=func.lower()
#         return lowercase
#     return wrapper
# def upper_case(function):
#     def wrapper():
#         func=function()
#         lowercase=func.upper()
#         return lowercase
#     return wrapper
# def capes(function):
#     def wrapper(ag1,ag2):
#         ag1 = ag1.capitalize()
#         ag2 = ag2.capitalize()
#         func=function(ag1,ag2)
#         return func
#     return wrapper
# @upper_case
# @lower_case 
# def hello():
#    return 'Hello World'

# @capes
# def cap(ag1,ag2):
#     return "Hell!!"+ag1+"Hi!!"+ag2
# print(hello())
# print(cap("dinesh","murugesan"))

'''lamda functions'''

# def multi_play(n):
#     return lambda a: a*n
# double=multi_play(2)
# trible=multi_play(3)
# print(double(10))
# print(trible(10))

'''lamda function in variables'''
# lamb=lambda a,b,c:a*b*c
# print(lamb(1,2,3))


'''count the max occurance'''
l=[2,3,4,6,7,2,3,3,5,6]

# print(max(l,key=l.count))

'''List of dict '''
student=[{"name":"Dinesh","Age":23,"Rno":123},
         {"name":"Ganesh","Age":24,"Rno":123},
         {"name":"Ramesh","Age":23,"Rno":123},
         {"name":"Gogul","Age":23,"Rno":123}]

l={d["name"] for d in student for k,v in d.items() if d[k]==24}
print(l)
# # l=[]
# for i in student:
#     for j,y in i.items(): 
#         print(i[j])
#         l.append({j:i[j].upper()})
#         break

# print(l)

'''
issubclass() provided by python. 
The method tells us if any class is a child of another class by returning true or false accordingly.
'''
class Parent(object):
   pass   
 
class Child(Parent):
   pass   

# Driver Code
# print(issubclass(Child, Parent))    #True
# print(issubclass(Parent, Child))    #False
# obj1 = Child()
# obj2 = Parent()
'''We can check if an object is an instance of a class by making use of isinstance() method:'''
# print(isinstance(obj2, Child))    #False 
# print(isinstance(obj2, Parent))   #True

'''main function in python'''

def dummy():
   print("Hi Interviewbit!")
def main():
   print("This is Main function!")
if __name__=="__main__":
#    main()
#    dummy()
    
 '''check if all characters in the given string is alphanumeric'''
 
# print(("shuug233").isalnum())
# print(("shuug*233").isalnum())

import re 
# print(bool(re.match("[A-z0-9a-z]+$","shuug233")))
# print(bool(re.match("[A-z0-9a-z]+$","shuug2^%3")))

''''is digit first char'''
STR="112DINESH"
# print(STR[0].isdigit())
# print(bool(re.match("^[0-9]",STR)))

'''random numbers'''

# import random as ra
# print(ra.random())
# print(ra.randrange(1,100,2))

'''covert int without int()'''

# def string_to_int(st):
#    num=0
#    for char in st:
#       for i in range(10):
#          if str(i)==char:
#             # print(num)
#             num=num*10+i
#    return num        

# print(string_to_int("474848"))


'''Zip and enumerate function'''

# arr1=[1,2,3,4,5,6,7]
# arr2=[8,5,6,9,3,5,3]
# arr3=[5,6,7,8,2,3,4]

# # print(list(zip(arr1,arr2,arr3)))

# for e1,e2,e3 in zip(arr1,arr2,arr3):
#    print(e1,e2,e3)

# for i,ele in enumerate(arr1,start=10):
#    print(i,ele)


'''string '''
str1="dinesh salem"
# print(type(str1.split()))

# def reverse(l):
#     r=""
#     for i in l:
#         r=str(i)+r
#     return r    
    
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reverse(l))
   
