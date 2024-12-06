arraylist={"arr1":[2,42,5,36],"arr2":[12,14,45,16],"arr3":[12,44,15,16]}

def arraeycombaincall(arraylist):
    orlist=[]
    for arr in arraylist.values():
        orlist.extend(arr)
    return orlist
def sortarraylist(arl):
    orlist=list(set(arraeycombaincall(arl)))
    for i in range(len(orlist)):
        for j in range(i+1,len(orlist)):
            if orlist[i]>orlist[j]:
                orlist[i],orlist[j]=orlist[j],orlist[i]
    return orlist

# print(sortarraylist(arraeycombaincall(arraylist)))
print(sortarraylist(arraylist))


