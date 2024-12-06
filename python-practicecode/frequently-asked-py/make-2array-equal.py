def canBeEqual(target,arr):
        if arr==target:
                return arr
        d={v:k for k,v in enumerate(target)}
        l=[i for i in range(len(target))]
        for i in arr:
                if i in d.keys():
                        l[d[i]]=i
                else: return False            
        return l==target 

def canBeEqual2(target,arr):
        d={ i:target.count(i) for i in (target)}
        d2={ i:arr.count(i) for i in (arr)}
        print(d,d2)
        if d==d2:
            return True
        else:
               return False
                           
target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual2(target,arr))
target = [1,2,2,3]
arr = [1,1,2,3]        
print(canBeEqual2(target,arr))
target = [3,7,9]
arr = [3,7,11]
print(canBeEqual2(target,arr))