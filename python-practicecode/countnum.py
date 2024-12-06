
##counr the repeating number 
# list=[1,1,3,4,4,6,6,8,5,7,10,10,"dinesh","dinesh"]
# out={}
# for i in list:
#     out[i]=(list.count(i))
# # print([k for k,v in out.items()])
# print(out)

# ------------------------------------
##counr the repeating number method 2
# list=[1,1,3,4,4,6,6,8,5,7,10,10]
# k={}
# for i in list:
#     if i in k:
#         k[i]+=1
#     else:
#          k[i]=1
# print(k)       

# -----------------------------
# reverse numbers
# list=[1,2,3,4,5,7,6,9,8,10]
# print(list[::-1])

# -------------------------
# #reverse string
# name='dineshkumar'
# str=''
# for i in name :
#     str=i+str
# print(str)
# --------------------------
#reverse list
# l=[1,2,3,4,5,6,7,8,9,10]

# left=0 
# right=len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)    
# ----------------------
# list Comprehension

# l=[i for i in range(1,10) if i<5]
# d={i:1 for i in range(1,10) if i<5}
# print(l)
# print(d)


##lamda
# x=lambda x,y,z:x+y+y
# print(x(1,2,3))

# print(5/2) #/ represents precise division (result is a floating point number) ##2.5
# print(5//2) #whereas // represents floor division (result is an integer) ##2
# print(5%2) # gives the remainter value 

#------------swapcase-------------
# string = "GeeksforGeek

'''------------------------''''try catch finnally'''' -------------'''

# try:
#   x=10/0
# except:
#   print("Something went wrong")
# else:
#    print("this is DINESH")  
# finally:
#   print("The 'try except' is finished")

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# y="Hello"
# if not type(y) is int:
#   raise TypeError("Only Int is Allowed")


##--------------*args and **kwargs---------------

# class argscheck:
#     def myFun1(*args):
#      for value in args:
#         print(value)

#     def myFun(arg1,*args):
#      print("first value",arg1)
#      for value in args:
#         print(value)

#     def myFun2(**kwargs):
#         for key, value in kwargs.items():
#             print("%s == %s" % (key, value))


#     # Driver code
# argscheck.myFun2(first='Geeks', mid='for', last='Geeks')
# argscheck.myFun1("dinesh","karthi",2,3)
# argscheck.myFun("dinesh","karthi",2,3)

#-------------tuple

# my_dict = {i:i+7 for i in range(1, 10)}
# print(my_dict)

# '''tuple comprehension is not posible its end up with generator'''
k=(i for i in (1, 2, 3))
# print(k)
# for i in k:
#     print(i)

###------------------Decorators----------

# class Decor:
#     def make_pretty(func):
#     # define the inner function 
#         def inner():
#         # add some additional behavior to decorated function
#             print("I got decorated")

#         # call original function
#             func()
#     # return the inner function
#         return inner

#     # define ordinary function
#     def ordinary():
#         print("I am ordinary")
        
#     # decorate the ordinary function
#     decorated_func = make_pretty(ordinary)

#     # call the decorated function
#     decorated_func()      


'''decorator------------with @'''
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_prettyrandon
# def ordinary():
#     print("I am ordinary")
# ordinary() 



####-----------------decorator-----------

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

# def smart_up(func):
#     def inner(a):
#         print("I am going to upper", a)
#         print(a.upper())
#         if a == " ":
#             print("Whoops! cannot upper")
#             return
#         return func(a)
#     return inner

# @smart_divide
# def divide(a, b):
#     print(a/b)
# @smart_up
# def upper(st):
#     print(st)


# divide(2,5)
# divide(2,0)
# upper("dinesh")
# upper(" ")



# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# # print(x)


'''--------------pickle and unpickle'''

import pickle
data={"name":"dinesh","age":24,"city":"salem"}

###pickling-- is converting python object into the byte files 
with open("data.pkl","wb") as file:
    pickle.dump(data,file)

###unpickling---is converting byte files into python object 
with open("data.pkl","rb") as file:
    loaddata=pickle.load(file)
print(loaddata)


'''# from tkinter import *'''

# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()
# from tkinter import *

# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()




# sort the list
# l=[1,4,3,8,5,9,20]
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>=l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l[-2])  


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




""" Print The Repeate Number"""
l=[1,2,3,4,4,5,6,7,6,10,10,10]
k={}
### Print("------ Dinesh ------")
for i in l:
    if i in k:
        k[i]=k[i]+1
    else:
        k[i]=1
'''frequent number of times'''
# print([num for num,i in k.items() if i >= 3]) 
print(k)

id=[1,2,3,4]
name=["dinesh","karthi","mari","kabilan"]
salary=["10","20","30","40"]

dict={key:[name,salary] for key,name,salary in zip(id,name,salary)}
print(dict)



d={"mari":30,"mari":100,"karthi":50,"dinesh":30,"dinesh":30}


# print([1,2,3]*5)

# from flask import Flask

# app=Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello world!"
    
# if __name__=="__main__":
#     app.run()



def insec(x,y):
    # l=
    # set1=set(x)
    # set2=set(y)
    # set3=set1.intersection(set2)
    return list(set(x)&set(y))

x=[1,5,9,0]
y=[3,0,2,9]
print(insec(x,y))


a=0
for i in [1,2,3]:
    a+=i
print('ansewr+ ',str(a))

print(type(())) 