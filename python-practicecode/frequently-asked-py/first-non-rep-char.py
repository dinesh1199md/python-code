

def first_non_rep_char(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    word=[k for k,v in dic.items() if v==1] 
    if word:   
        return list(s).index(word[0]),word
    else:
       return -1
    


    
def method(s):    
    curr = list(s)
    for i in range(0,len(s)):
        if curr.count(s[i]) == 1:
            return i
    return -1

            
s="eeshh"
print(first_non_rep_char(s))

print(method(s))