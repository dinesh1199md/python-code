def merge(l1,l2):
    # max_l=max(len(l1),len(l2))
    # l1+=[0]*(max_l-len(l1))
    # l2+=[0]*(max_l-len(l2))
    
    while len(l1)!=len(l2):
        if len(l1) > len(l2):
            l2.append(0)
        elif len(l1) < len(l2):
            l1.append(0)    
    f=[]
    for i in zip(l1,l2):
        f.append(sum(i))
    return f    
print(merge([1,2,3],[1,2,3,4]))


