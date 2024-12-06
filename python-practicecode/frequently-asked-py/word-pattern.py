def wordpattern(pattern,l):
    d={}
    s=l.split(" ")
    # print(s)
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=pattern[i]
        elif d[s[i]]!=pattern[i]:
            return False
    print(d)
    return True    

def wordPattern(pattern, s):
        words = s.split()
        hashmap = {}

        for word, pattern_char in zip(words, pattern):
            if pattern_char in hashmap:
                if hashmap[pattern_char] != word:
                    return False
            elif word in hashmap.values():
                return False 
            hashmap[pattern_char] = word
        print(hashmap)
        return True 
p="abba"
l="dog cat cat dog"
# print(wordpattern(p,l))
print(wordPattern(p,l))