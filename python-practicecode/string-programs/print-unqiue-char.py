def unque(s):
    d={}
    for i in s:
        if i not in d :
            d[i]=1
    return "".join(d.keys())
print(unque("Java Automation"))
 
def unque2(s):
    d={}
    # for i in s:
    #     if i not in d :
    #         d[i]=1
    return set(s)

print(unque2("Java Automation"))