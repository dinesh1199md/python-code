def anagram1(s1,s2):
    return sorted(s1)==sorted(s2)
print(anagram1("eat","ate"))

def anagram2(s1,s2):
    d={}
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j in s1:
        if j in d:
            d[j]-=1
        else:
            d[j]=1
    return not bool([i for v in d.values() if v!=0])
print(anagram2("eatt","aste"))