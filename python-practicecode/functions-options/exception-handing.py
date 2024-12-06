def zeroexception(a,b):
    try:
        c=a/b
        print(f"the divisio value",c)
    except ZeroDivisionError:
        print("Error")    
        
# zeroexception(10,0)        
def zerocheck(func):
    def wrapper(a,b):
        print("start")
        if a!=0:
         res= func(a,b)
         return res
        else: print("Change the input values")
        return -1
    return wrapper        

@zerocheck
def zeroexception_decorator(a,b):
    c=a/b
    print(f"the divisio value",c)
# zeroexception_decorator(10,2)


class Sollutions:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def disply(self):
        print(f"vaules of a: {self.a} and b: {self.b}")

    def update(self,a,b):
        self.a=a
        self.b=b    
        # print(f"vaules of after update  a: {self.a} and b: {self.b}")

obj1=Sollutions(10,20)
obj1.disply()
obj1.update(100,200)
obj1.disply()


'''binary search on sorted array'''
def binarysearch(l,target):
    left,right=0,len(l)-1
    while left<=right:
        mid=(right+left)//2
        if l[mid]==target:
            return mid
        elif(l[mid]<target):
            left=mid+1
        else:
            right=mid-1    
    return -1
print(binarysearch([1,2,3,4,5],5))


