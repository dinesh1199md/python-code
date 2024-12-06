def inplace(l1,l2):
    while len(l1)!=len(l2):
        if len(l1)>len(l2):
            l2.append(0)
        elif len(l1)<len(l2):
            l1.append(0)    
    # print(l1,l2)        
    out=[]
    for i in zip(l1,l2):
        out.append(sum(i))
    return out

print(inplace([1,2,3,5,9,7,2],[1,2,3]))

