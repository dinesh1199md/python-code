def anagram1(s1,s2):
    return sorted([s for s in s1])==sorted([s for s in s2])

def anagram2(s1,s2):
    lis=[i for i in s1]
    c=0
    for j in s2:
        if j in lis:
            c+=1   
    return c==len(lis)       


def anagram3(s1,s2):
   d={}
   for i in s1:
       if i in d:
           d[i]+=1
       else: d[i]=1
   for i in s2:
        if i in d:
            d[i]-=1
        else: d[i]=(-1)   
   print(d) 
   return not bool([v for v in d.values() if v!=0])
print(anagram3("a","ab"))
print(anagram1("a","ab"))

