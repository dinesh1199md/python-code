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

 
print(merge_sorted_lists([1,3,5],[2,4,6]))