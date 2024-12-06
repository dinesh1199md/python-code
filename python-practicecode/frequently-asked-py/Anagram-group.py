def group_anagram(list1):
    group={}
    for word in list1:
        sorted_word="".join(sorted(word))
        if sorted_word in group:
            group[sorted_word].append(word)
        else:
            group[sorted_word]=[word]
    print(group)        
    return list(group.values())
print(group_anagram(["eat","tea","tan","ate","nat","bat"]))




