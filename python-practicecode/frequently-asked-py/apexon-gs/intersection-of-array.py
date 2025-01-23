

def intersection(a1,a2):
    # return set(a1)&set(a2)
    if len(a1)>len(a2):
        o=a2
        inn=a1
    else:
        o=a1
        inn=a2
    
    out=[]
    for i in range(len(o)):
        for j in range(len(inn)):
            if o[i]==inn[j]:
                out.append(o[i])
                inn.pop(j)
                break
    return out

a2=[1,1,2,2,2]
a1=[1,1,1,2,2,3,4,5]
# Output: [1,1,2,2]
print(intersection(a1,a2))