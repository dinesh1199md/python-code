# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def removeduplicate(l):
    seen=set()
    count=0
    for i in l:
        if i not in seen:
            seen.add(i)
        else:
            count+=1
    # out=list(seen)+[ f"_" for i in range(count)]
    out=sorted(list(seen)      )
    
    if  out:
        return out
    else:
        return -1
      


nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
print(removeduplicate(nums))

def containsDuplicate(nums):
        seen=set()
        for i in nums:
            if i not in seen:
                print(seen)
                seen.add(i)
            else:
                return True
        return False  

print(containsDuplicate([1,2,3,4]))