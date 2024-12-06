
def missingnum(l):
    misnum=(set(i for i in range(min(l),max(l)+1))-set(l))
    return list(misnum)

def missingnum2(l):
    n=len(l)+1
    tnum=(n*(n+1))//2
    print(tnum)
    ssum=sum(l)
    print(ssum) 
    return tnum-ssum

# print(missingnum([11,12,14]))
# print(missingnum2([1,2,4]))