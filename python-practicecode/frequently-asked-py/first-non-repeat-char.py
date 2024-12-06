def first_non_repeating_char(ss):
    str_dict={}
    for s in ss:
        if s in str_dict:
            str_dict[s]+=1
        else:
            str_dict[s]=1    

    for index,char in enumerate(str_dict):
        if str_dict[char]==1:
            return char,index
    return None,-1 
s="swiss"
char,index=first_non_repeating_char(s)
print(first_non_repeating_char(s))

if char:
    print(f"the first non repeating char is : {char} and index is: {index}")
else:
    print(f"the first non repeating char is not found")
