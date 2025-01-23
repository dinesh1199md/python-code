def test(l):
    c=1
    st=""
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            c+=1
        else:
            st+=l[i-1]+str(c)
            c=1 
    st+=l[-1]+str(c)
    print(st)
    
test("aabbbcaadd")

def test2(l):
    st=""
    for i in range(0,len(l),2): 
        st+=l[i]*int((l[i+1]))
    print(st)   
    
test2("a2b3c1a2d2")