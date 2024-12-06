

def rev(l):
    # return l[::-1]
    k=len(l)
    n=k//2
    for i in range(n):
        print( l[i],l[k-1-i])
        l[i],l[k-1-i]=l[k-1-i],l[i]
    return l

l=['h',"e","l","o"]
print(rev(l))
