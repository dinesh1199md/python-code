
def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        # print(i)
        fact *= i
    return fact
print(factorial(5))

# RECURSION
'''it is a process in which a function calls itself directly or indirectly. '''
def fact_recursion(n):
    if n < 1:
        return 1
    else:
        return n * fact_recursion(n-1)
    
print(fact_recursion(1))

def fact2(n):
    if n<1:
        return 1
    else:
        return n*fact2(n-1)
print(fact2(5))





