

def vow(s):
    d={}
    v=['a','e','i','o','u']
    for i in s:
        if i in d:
            if i in v:
                d[i]+=1
        else:
            d[i]=1
    return list({k:v for k,v in sorted(d.items(),key=lambda e:-e[1])}.items())[0]
    # max(d,key=d.get)
print(vow('amruthiaaaiii'))

def common(l):
    l2=[]
    for word in zip(*l):
        if len(set(word))==1:
            l2.append(word[0])
        else:
            break
    return ''.join(l2)

print(common(['flag','flute','flower']))


