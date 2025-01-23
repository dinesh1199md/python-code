

def max_char(s):
    cur_c=1
    max_c=0
    res=''
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cur_c+=1
        else:
            if cur_c > max_c:
                max_c=cur_c
                res=s[i-1]
            cur_c=1
    if  cur_c > max_c:
        max_c=cur_c
        res=s[i-1]
    return res
print(max_char("aaabbb")) 