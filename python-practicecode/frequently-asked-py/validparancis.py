def checkvalid(s):
    stack=[]
    checkdict={")":"(","}":"{","]":"["}

    for char in s:
        print(stack)
        if char in checkdict.values():
            stack.append(char)
        elif char in checkdict.keys():
            # print(char)
            if not stack or checkdict[char] != stack.pop():
                return False
    # print(stack) 
    return not stack   

print(checkvalid("({{{{}}}))"))