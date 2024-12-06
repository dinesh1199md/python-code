from collections import Counter

def method1(my_list):
    l=Counter(my_list)
    print(l)
    return  max(l,key=l.get)



def method2(my_list):
    d={}
    for i in my_list:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)        
    sortdic={k:v for k,v in sorted(d.items(),key=lambda e:e[1])}.keys() # -e[0] means decending order
    print(sortdic)
    return list(sortdic)[-1]
    # return [k for k,v in sorted(d.items(),key=lambda e:e[1]) if k==1]

def dub(my_list):
    d={}
    # dub=[]
    for i in my_list:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)
    return [k for k,v in d.items() if v>=3]        

my_list = [1, 2, 3, 2, 1,3, 3, 1, 2, 3, 4, 5]
# print(method1(my_list))
print(method2(my_list))
# print(dub(my_list))