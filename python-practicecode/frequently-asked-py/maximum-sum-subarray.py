class Solution:
    def maxSubArray(self,nums):
        currentmax=nums[0]
        maxsum=nums[0]

        for num in nums[1:]:
            currentmax=max(num,currentmax+num)
            maxsum=max(currentmax,maxsum)
        return maxsum    

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# print(sum([-2,1,-3,4,-1,2,1,-5,4]))

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


 