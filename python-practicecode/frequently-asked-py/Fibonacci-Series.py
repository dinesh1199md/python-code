
#  0 1 1 2 3 5 8 13 21 
# from functools import lru_cache


'''this will return the value of the series bassed on the position'''
# @lru_cache
def fib(n):
    if n<0:
        return "incorrect element"
    elif(n==1 ):
        return 0
    elif(n==2 ):
        return 1
    else:
        return fib(n-1)+fib(n-2) 

print("fib",fib(10))    
# #  0 1 1 2 3   5 8 13 21 
    
'''This will gerate the series up to the given number count'''    
def febseries(num):
    f,s=0,1
    for i in range(num):
        if i<=1:
            result=i
        else:
            result=f+s
            f=s
            s=result
        print(result,end=" ")    
# febseries(5)


'''recursive way of fibonacci series'''
def febrecur(num):
    if num==0: return 0
    elif num==1: return 1
    else:
        return febrecur(num-1)+febrecur(num-2)

for i in range(5):
    print(febrecur(i))





def fib(n):
    a,b=0,1
    if n<=0:
        return 0
    print(a,end=" ")
    for i in range(1,n):
        print(b,end=" ")
        a,b=b,b+a
        
def fib2(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fib2(n-1)+fib2(n-2)
# fib(10)
print (f"fib2")
# print(fib2(10))
for i in range(10): 
    print(fib2(i),end=" ")


def fib_gen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fibb=fib_gen()
# for i in range(10):
#     print(next(fibb),end=" ")

