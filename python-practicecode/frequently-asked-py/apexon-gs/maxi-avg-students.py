def say_hello(a):
    d={}        
    for i in a:
        key=i[0]
        v=int(i[1])
        if key in d:
            d[key][0]+=v
            d[key][1]+=1
        else:
             d[key]=[v,1]

    res=0
    for k,v in d.items():
        # res=max(res,v[0]//v[1])
        temp=(v[0]//v[1])
        if temp>res:
            res=temp
    print(d)
    print(res)
    return res
    

a= [
        ("Bob", "87"), ("Mike", "35"),
        ("Bob", "52"), ("Jason", "35"),
        ("Mike", "55"), ("Jessica", "99")
    ]
say_hello(a)