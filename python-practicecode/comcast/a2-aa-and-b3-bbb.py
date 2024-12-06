def unpack(l):
    d=[]
    for i in l:
        d.append(i[0]*int(i[1])) 

    return d
print(unpack(["A2","B3","C4"]))


def pack(l):
    d={}
    for i in l:
            d[i[0]]=len(i)
    return [k+str(v) for k,v in d.items()]
print(pack(["AA","BB","CCCC"]))