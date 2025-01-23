def merg_miden(l1,l2):
    sortl=[]
    i=0
    j=0
    while i< len(l1)and j<len(l2):
        if l1[i]<l2[j]:
            sortl.append(l1[i])
            i+=1
        else:
            sortl.append(l2[j])
            j+=1
            
    sortl.extend(l1[i:])
    sortl.extend(l2[j:]) 
    
    n=len(sortl)
    mid=n//2
    if n%2==0:
      m=(sortl[mid]+sortl[mid-1])/2
    else:
      m=sortl[mid]
    return m  
        
num1=[1,3]
num2=[2,4]
print(merg_miden(num1,num2))
num1=[1,3]
num2=[2]
print(merg_miden(num1,num2))