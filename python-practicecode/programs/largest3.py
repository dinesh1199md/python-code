def large3(a,b,c):
    if (a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    return largest            
print(large3(10,3,45))