def code(w):
    l=[]
    for i in w:   
        l.append(chr(ord(i)+2))
    return "".join(l)    

w="AA"
print(code(w))