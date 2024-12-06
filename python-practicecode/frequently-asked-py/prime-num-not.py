
def primecheck(num):
    c=0
    if num>1:
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
    if c==2:
        # print(f"The given: {num} numer is Prime")
        return True
    else:    
        # print(f"The given: {num} numer is not a Prime")
        return False

# print(primecheck(17))


def is_prime_trial_division(n):
  
    # Check if the number is less than
    # or equal to 1, return False if it is
    if n <= 1:
        return False
      
    # Loop through all numbers from 2 to
    # the square root of n (rounded down to the nearest integer)
    # print(range(2, int(n**0.5)+1))
    for i in range(2, int(n**0.5)+1):
        # If n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
    # If n is not divisible by any of these numbers, return True
    return True

# Test the function with n = 11
# print(is_prime_trial_division(11))

def countPrimes(n: int) -> int:
        c=0
        if n<=1: return 0
        l=[i for i in range(1,n+1)]
        for i in l:
            if is_prime_trial_division(i):
                print(i)
                c+=1
        return c       
print(countPrimes(10) )


def countPrimes2( n: int) -> int:
        c=0
        if n<=1: return 0
        l=[i for i in range(1,n+1)]
        for num in l:
            c1=0
            if num>1:
                for i in range(1,num+1):
                    if(num%i==0):
                        c1+=1
            if c1==2:
                c+=1
        return c 
# print(countPrimes2(3) )