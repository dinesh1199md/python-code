# strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

def longestCommonPrefix(v):
    ans=""
    v=sorted(v,key=lambda e:len(e))
    print(v)
    first=v[0]
    last=v[-1]
    for i in range(len(first)):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans

def longest_common_prefix(strings):
    prefix = []
    for chars in zip(*strings):
        print(set(chars))
        if len(set(chars))==1:
            prefix.append(chars[0])
        else:
            break
    # return "".join(prefix)
    return "".join(prefix) if  prefix  else -1

# strings = ["flower", "flow", "flight"]
# prefix = longest_common_prefix(strings)
# print(prefix)


strs = ["flower","flow","flowm","flight"]
print(longestCommonPrefix(strs))