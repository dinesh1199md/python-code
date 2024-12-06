def intersecarray(l1,l2):
    s1=set(l1)
    inlist=[]
    for i in l2:
        if i in s1:
            inlist.append(i)
            s1.remove(i)
    return inlist        

# print(intersecarray([1,1,3],[2,1,3,2]))
print(intersecarray([1,2,2,1],[2,1,2]))
print(set([1,2,2,1])&set([2,1,2]))
