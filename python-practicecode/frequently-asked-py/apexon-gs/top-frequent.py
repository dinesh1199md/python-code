def top_k_frequent(words, k):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1



    wfd = list(frequency.items())
    # print(wfd)
    
    # Bubble sort based on frequency and lexicographical order
    n = len(wfd)
    for i in range(n):
        for j in range(i+1, n ):
            # Sort by frequency in descending order; if equal, sort lexicographically
            if (wfd[i][1] <  wfd[j][1]) or (
               (wfd[i][1] == wfd[j][1] and wfd[i][0] > wfd[j][0])):
                # Swap elements
                wfd[i], wfd[j] = wfd[j], wfd[i]
    # print(wfd)
    result = [word for word, _ in wfd[:k]]
    return result

# Input
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

# Get the result
result = top_k_frequent(words, k)

# Output the result
print(result)
















def topKFrequent0(words, k):
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
            
        # return sorted(sorted(freq), key=freq.get, reverse=True)[:k]
        print(d)
        print(sorted(d))
        print(sorted(sorted(d), key=d.get,reverse=True)[:k])
        return [k for k,v in sorted(sorted(d.items()),key= lambda x:-x[1])][:k]
    
    
def topKFrequent2(words,k):
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
            
        res= sorted(d,key= lambda x:(-d[x],x))
        return res[:k]
    
words =["i","love","leetcode","i","love","coding"]
k = 3

print(topKFrequent0(words,k))




