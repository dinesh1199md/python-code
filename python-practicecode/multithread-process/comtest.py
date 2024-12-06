

# def valid_check(s):
#     d={"}":"{",")":"(","]":"["}
#     stack=[]
#     for c in s:
#         if c in d.values():
#             stack.append(c)
#         elif c in d.keys():
#             if not stack or d[c] != stack.pop():
#                 return False
#     return not stack
    
# print(valid_check("{[()]}"))



# Input: "{[()]}"
# # Output: True
 
# Input: "{[(])}"
# # Output: False

def plain(a):
    l=[]
    for i in a:
        if isinstance(i,list):
            l.extend(plain(i))
        else:
            l.append(i)
    return l
Arr = [1, 2, [3, 4, [5, 6]]]
print(plain(Arr))

# output = [1,2,3,4,5,6]
 
 
 
# def same(a,b):
#     seen=set(b)
#     out=[]
#     for i in a:
#         if i in seen:
#             out.append(i)
#             seen.remove(i)
#     return out

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6] 
# print(same(a,b))

# print(set(a)&set(b)) 
# # out = [3,4]