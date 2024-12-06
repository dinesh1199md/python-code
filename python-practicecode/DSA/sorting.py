def buble_sort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l            
l=[2,0,2,1,1,0]
# print(buble_sort(l))

def pointer_sort(l):
    le,r=0,1 
    while l[le]>=l[r]:
        print(l[le],l[r])
        l[le],l[r]=l[r],l[le]
        le+=1
        r+=1
    return l
l=[2,0,2,1,1,0]
print(pointer_sort(l))