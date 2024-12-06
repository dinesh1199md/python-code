# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=0
        r=len(s)-1
        sl=list(s)
        while l<r:
            if sl[l].isalpha():
                if sl[r].isalpha():
                    sl[l],sl[r]=sl[r],sl[l]
                    l+=1
                    r-=1
                else:
                     r-=1
            else:
                l+=1
        # print(sl)
        print("".join(sl))    
obj1=Solution().reverseOnlyLetters("09ab9cd")        






