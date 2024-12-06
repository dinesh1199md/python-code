def pre_add(l):
    o=[]
    for i in range(len(l)):
        if i==0:
            o.append(l[0])
        else:
            o.append(sum(l[:i+1]))
    return o        

def pre_add2(l):
    pre=0
    o=[]
    for i in l:
        o.append(pre+i)
        pre+=i
    return o
        
l=[1,2,3,4,5]
print(pre_add(l))
print(pre_add2(l))
# print(l[:5])