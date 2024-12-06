def sub_string(s):
    st=0
    e=1
    max_l=0
    d={}
    while e<=len(s):
        if len(s[st:e])==len(set(s[st:e])):
            cur_l=len(s[st:e]) 
            d[s[st:e]]=len(s[st:e])
            max_l=max(max_l,cur_l)
            e+=1
        else:
            st+=1
    return max_l,[k for k,v in sorted(d.items(),key= lambda e:e[1])][-1]
s = "bbbb"
print(sub_string(s))