def reverse(y: int) -> int:
        rev=0
        # int_max=2**31 -1
        x=abs(y)
        while(x>0):
            n=x%10
            # if rev> (int_max-n)//10:
                 # x causes the value to go outside the signed 32-bit integer 
                 # range [-231, 231 - 1], then return 0.
                # return 0
            rev=rev*10+n
            x=x//10
        result= rev if y>0 else - rev     
        return result
print(reverse(-120))

# Example 1:
# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21