
def merge_sorted_lists(l1, l2):
  fa=[]
  i,j=0,0
  while i< len(l1) and j< len(l2):
    if l1[i] < l2[j]:
      fa.append(l1[i])
      i+=1
    else:
      fa.append(l2[j])
      j+=1
  fa.extend(l1[i:])
  fa.extend(l2[j:])
  return fa
# print(merge_sorted_lists([1,3,5],[2,4,6]))


def median(num1,num2):
    l=sorted(num1+num2)
    # l=merge_sorted_lists(num1,num2)
    n=len(l)
    mid=n//2
    if n%2==0:
        median=(l[mid]+l[mid-1])/2
        return median
    else:
        median=l[mid]
        return median

num1=[1,3]
num2=[2]
print(median(num1,num2))
num1=[1,2]
num2=[3,4]
print(median(num1,num2))



# ---------------------------meiden of sorted lists----------------------------------------------------------------

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