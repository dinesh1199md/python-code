
array = [1, 2, 2, 3, 3, 4]
def freq(array, k):
    arrayset = set(array)
    dict1 = {}
    result = []
    for i in arrayset:
        dict1[i] = array.count(i)
        if dict1[i] >= k:
            result.append(i)
    return result

def method2(array, k):
    dict1 = {}
    for i in array:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(dict1)        
    return [key for key, count in dict1.items() if count >= k]



# print(freq(array, 2))
print(method2(array, 2))

from collections import Counter
def highest_frequency(arr):
    count = Counter(arr)
    return max(count, key=count.get)
arr = [1, 2, 3, 4, 5, 3, 2, 2]
print(highest_frequency(arr))
