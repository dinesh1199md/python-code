def dublicate(l):
    s=[]
    dub=[]
    for i in l:
       if i  not in s:
         s.append(i) 
       else:
         dub.append(i)    
    print(s)         
    return dub    
print(dublicate([1,2,3,4,4,5,6,7,8,9,10,10]))

# if bool(dublicate([1,2,3,4,4,5,6,7,8,9,10,10])):
#    print("I")
   

#reverse number
# print(int(str("230")[::-1]))