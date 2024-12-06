class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return  [i,j]

    def twoSum1(self,nums,target):
        comlis=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    if(nums[i],nums[j]) not in comlis:
                        comlis.append((nums[i],nums[j]))
        if comlis:return comlis 
        else:return -1

    def twoSum11(self,nums,target):
        comlis=[]
        right=nums[0]
        for i in nums:
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    if(nums[i],nums[j]) not in comlis:
                        comlis.append((nums[i],nums[j]))
        if comlis:return comlis 
        else:return -1
                  

# print(Solution().twoSum([3,2,3,2,4],6))
print(Solution().twoSum11([1,1,2,2,4,5,6,7,8,9],14))


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 