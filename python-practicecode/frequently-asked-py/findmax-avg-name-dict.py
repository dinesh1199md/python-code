def avgcal(d):
    temp={}
    count={}
    for name in d:
        if name[0] in temp:
            temp[name[0]]+=int(name[1])
            count[name[0]]+=1
        else: 
            temp[name[0]]=int(name[1])
            count[name[0]]=1
    final={}
    for i,j in zip(count.keys(),temp.keys()):
        if i==j:
            final[i]= temp[i]/count[i]
        else: final[i]= temp[i]/count[i]
    print(temp)
    print(count)
    print(final)
    out={k:v for k,v in sorted(final.items(),key= lambda e:-e[1])}
    return list(out.items())[0]

d=[["mari","30"],["mari","100"],["karthi","51"],["dinesh","31"],["dinesh","32"]]
print(avgcal(d))
# s=sorted(d,key=lambda x:(x[1]))
# print(s)