def sortlist(l):
    ordict={}
    for w in l:
        if w in ordict:
            ordict[w]+=1
        else:
            ordict[w]=1    
    # print([k for k,v in sorted(ordict.items(),key=lambda e: -e[1])])
    return [k for k,v in sorted(ordict.items(),key=lambda e: -e[1])]
print(sortlist(["apple","banana","orange","banana","apple","zebra","zebra","zebra"]))

