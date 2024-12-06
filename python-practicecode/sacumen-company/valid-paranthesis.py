def valid_para(p):
    stack=[]
    d={")":"(","}":"{","]":"["}

    for i in p:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            print(d[i])
            if not stack or d[i] != stack.pop():
                return False
        
    return  not stack

def valid_para2(p):
    stack=[]
    d={")":"(","}":"{","]":"["}
    for char in p:
        if char in d:
            top_ele= stack.pop() if stack else "#"
            if  d[char] != top_ele:
                return False
        else: 
            stack.append(char)
    return  not stack

p="{}}"
print(valid_para2(p))