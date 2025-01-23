
def breakloop(n):
    c=0
    for i in range(1,len(n)):
        if n[i]==n[i-1]:
            c+=1
        else:
            if c!=1:
                print (f"{n[i-1]}-{c} times")
            elif(c==1):
                print (f"{n[i-1]}-{c} times")
                break
            c=1
            
(breakloop([1,1,1,9,9,9,4,1,1]))

