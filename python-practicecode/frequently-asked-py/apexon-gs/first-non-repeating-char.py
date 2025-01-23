

def non_repeat_ch(s):
    for i in range(len(s)):  
        flag=False
        for j in range(len(s)):
            if i!=j and s[i]==s[j]:
                flag=True
                print(flag)
                break
        if not flag:
            return s[i]
    return 0

print(non_repeat_ch("eggg"))