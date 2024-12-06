l=[2,4,5,0,0,6,0,10,3]

def movezero(l):
    for i in l:
        if i==0:
            l.remove(i)
            l.append(i)         
    return l
print(movezero(l))           