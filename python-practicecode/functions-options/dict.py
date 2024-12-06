dict11={"a":1,"b":2,"c":3}

print([min([v for k,v in dict11.items()])])
print(dict11.get("d")) #this will give None

# print(dict["d"]) #this will throw the Keyerror
# dict.pop("a")
print(dict11)
'''adding new key-value'''
dict11["d"]=4
'''modifying existing key-value'''
dict11["d"]=10
'''delete key-value'''
del dict11["c"]


'''#merg two dict'''
def add2dict(d1,d2):
    return {**d1,**d2}
def add2dict_m2(d1,d2):
    merge_dict=d1
    merge_dict.update(d2)
    return merge_dict

dict1 = {"a": 1, "b": 2,"c":10}
dict2 = {"b": 3, "c": 11}
print(add2dict(dict1,dict2))
print(add2dict_m2(dict1,dict2))


a=["A1","B2","C3"]
print(dict(a))

color=[('red',1),('blue',2),('green',3)]
d=dict(color)
print (d)
def secondlargein_dict(new_dict):
    print([k for k,v in sorted(new_dict.items(),key=lambda e:e[1])][-2])
    k=[k for k,v in sorted(new_dict.items(),key=lambda e:e[1])][-2]
    # print(new_dict[k])
    return {k:new_dict[k]}
print (secondlargein_dict( {"google":12, "amazon":9, "flipkart":4, "gfg":13}))

