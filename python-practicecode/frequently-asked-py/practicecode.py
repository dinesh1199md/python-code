
def fun1():
    n=1
    while n<101:
        yield n
        n+=1
fun_call=fun1()
# for i in fun_call:
#     print(i,end=" ")

def fun2():
    n=1
    while True:
        yield n
        n+=1
fun_call2=fun2()
for _ in range(101):
    print(next(fun_call2),end=" ")
 


v=[i for i in range (1,101)]
# print([i for i in range (1,101)])
# print(v)
    
c=0
t=16
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i]+v[j]==t:
            c+=1
print(c)            





      
