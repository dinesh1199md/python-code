class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
    
print(Solution().romanToInt("IV"))    

'''int to roman'''
class Solution2:
    def intToRoman(self, num: int) -> str:
        map={"M": 1000,
	       "CM": 900,
	       "D": 500,
	       "CD":400,
	       "C": 100,
	       "XC": 90,
	       "L": 50,
	       "XL": 40,
	       "X": 10,
	       "IX": 9, 
	       "V": 5,
	       "IV": 4,
	        "I": 1}

        ans=""
        for k,v in map.items():
            while num>=v:
                ans+=k
                num-=v
        return ans
    
print(Solution2().intToRoman(15))        
            