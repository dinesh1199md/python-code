# Repeating first index. 


def first_repeat(s): 
    d={}
    inx=0
    for i in s:
        if i in d:
            # d[i]+=1
            return i,inx
        else:
            d[i]=1
            inx+=1

# "rahulgorai" - return r
print(first_repeat("rahulgorai"))