def duplicate_char(s):
    stri=[i for i in s if i!=" "]
    d={}
    for i in stri:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return {k:v for k,v in d.items() if v>1}   

print(duplicate_char("Learn java programming"))
