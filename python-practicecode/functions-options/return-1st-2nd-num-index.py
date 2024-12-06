
def repeating(l,t):
    l2=[]
    for i,v in enumerate(l):
        if v==t:
            l2.append(i)
    l3=[]       
    if l2 :
        l3.append((l2[0]))
        l3.append((l2[-1]))
    else: 
        l3=[-1,-1]
    return l3


def repeating2(l,t):
    i = 0
    j = len(l) - 1
    first, last = -1,-1
    while i <= j:
        if l[i] == t:
            first = i
        elif first == -1:
            i = i + 1
        if l[j] == t:
            last = j
        elif last == -1:
            j = j-1
        if first != -1 and last != -1:
            return first, last
    return first, last
          
print(repeating([5,7,7,8,8,10],5))