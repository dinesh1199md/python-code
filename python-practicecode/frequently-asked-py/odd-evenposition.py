# Example 1:
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Example 2:
# Input: nums = [2,3]
# Output: [2,3]



def sortArrayByParityII(nums):
    l1 , l2 = [] , []
    for num in nums:
        if num%2==0:l1.append(num)
        else:l2.append(num)  
    nums[0: 2*len(l1) : 2] = sorted(l1)
    nums[1: 2*len(l2) : 2] = sorted(l2)    
    return nums   

List=[4,2,5,7]        
print(sortArrayByParityII(List))
