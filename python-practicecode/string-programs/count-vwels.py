def ount_vow(s):
    v=["a","e","i","o","u"]
    vow=[]
    cons=[]
    for i in s:
        if i in v:
            vow.append(i)
        elif(i!=" "):
            cons.append(i)    
    return len(vow),len(cons)

print(ount_vow("Hello World"))      