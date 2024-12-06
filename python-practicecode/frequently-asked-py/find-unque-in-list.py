def unque(l):
    num=0
    for i in l:
        num=num^i
    return num
print(unque([1,2,2,3,3]))