def closest_value(l,t1):
    d={}
    for i in sorted(l):
        d[i]=abs(t1-i)
    f=[k for k,v in sorted(d.items(),key=lambda e:e[1])][0]
    print(f)
    print({k:v for k,v in sorted(d.items(),key=lambda e:e[1])})
    return f

def closest_value2(l2,t1):
    l=sorted(l2)
    return  l[min(range(len(l)),key=lambda i:abs(l[i]-t1))]
l=[1,4,7,9,2]
t1=3
# t2=5
print(closest_value(l,t1))


# from getpass import getpass
# print(getpass("Enter your password:   "))

