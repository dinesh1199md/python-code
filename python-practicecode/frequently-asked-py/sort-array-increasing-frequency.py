def sort_frquency(l):
    d={i:l.count(i) for i in set(l)}
    print(d)
    d2=sorted(d.items(),key=lambda e:e[1])
    print(d2)
    out=[str(i[0])*i[1] for i in d2]
    print(out)
    # k="".join(out)
    # print(list(k))
    re=[int(i) for i in "".join(out)]
    return re

print(sort_frquency([1,1,2,2,2,3,4,4,5,5,5]))