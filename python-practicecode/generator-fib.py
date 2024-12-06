def fin_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

# fin_generator()
fib_gen=fin_generator()
# range
for i in range(5):
    print(next(fib_gen),end=" ")
#infinte
# for i in fib_gen:
#     print(i)



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
