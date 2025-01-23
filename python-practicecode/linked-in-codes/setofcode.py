def frequency(l):
    max=l[0]
    min=l[0]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j] and l[i]!=0 and l[j]!=0:
                l[i],l[j]=l[j],l[i]
    return l

print(frequency([2,3,0,4,4,4,0,1,2,3,7]))


def max_min_sum(l):
    max=l[0]
    min=l[0]
    sum=0
    for i in l:
        sum+=i
        if i>max:
            max=i
        if i<min:
            min=i
            
    return max,min,sum



def second_max_min(l):
    f=float('-inf')
    s=float('-inf')
    fs=float('inf')
    ss=float('inf')
    for n in l:
        if n > f:
            s,f=f,n
        elif(n>s) and n!=f:
            s=n
        
        if n < fs:
            ss,fs=fs,n
        elif(n<ss) and n!=fs:
            ss=n
    return ss,s

print(second_max_min([2,3,4,4,4,1,2,3]))

# leading and trialing zero remove

def check(s):
    return s.strip('0') if  s.strip('0') else 0
    
print(check("00123"))

 