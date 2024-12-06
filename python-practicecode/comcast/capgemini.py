'''1. reverse the sentance'''

def method1(s):
    r=""
    print(s.split())
    for i in s.split():
        r=i+" "+r
    return r
    # print(r)
def method2(s):
    return " ".join(s.split(" ")[::-1])
    # print(r)
s="hello i am from salem"
print(method1(s))
print(method2(s))


'''2. fibonacci series'''
def fici(n):
    # while n>0:
    f,s=0,1
    for i in range(n):
        if i<=1:
            r=i
        else:
            r=f+s
            f=s
            s=r
        print(r,end=" ")
#fici(9)
 
def fici_r(n):
    if n==0: return  0
    elif n==1: return 1
    else:
        return fici_r(n-1)+fici_r(n-2)
# for i in range(5):  
#     print(fici_r(i),end=" ")

'''generator'''

def gen(n):
    for i in range(n+1):
        if i%2==0:
            yield i
        else:
            yield i
p=gen(10)
print(list((p)))

'''decotrators'''

c=0
def dico1(func):
    def inner(a,b):
        global c
        c+=1
        return func(a,b),c
    return inner

@dico1
def dic(a,b):
    return a+b

print(dic(10,20))
print(dic(10,30))
print(dic(10,10))

'''file handling'''
# def filehand(s):
#     try:
#         # with open("checkfile","+a") as file:
#         #     file.writelines(s)
#         s/s
#     except:
#         raise Exception("This is Unknown exception from code")
    
# filehand("this dinesh doing the code part")