
def sort_lis1_based_onlist2(list1,list2):
    final_dict={}
    for k,v in zip(list1,list2):
        final_dict[k]=v
    # print(final_dict)    
    return ([k for k,v in sorted(final_dict.items(),key= lambda item:item[1])])

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    # print (list(zipped_pairs))
    z = [x[1] for  x in sorted(zipped_pairs)]
    return z 

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print(sort_lis1_based_onlist2(list1,list2))
print(sort_list(list1,list2))


# Python3 code to demonstrate working of 
# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()

def maxi_min(test_tup,K):
    # initializing tuple
    # printing original tuple
    print("The original tuple is : " + str(test_tup))
    # Maximum and Minimum K elements in Tuple
    # Using slicing + sorted()
    test_tup = list(test_tup)
    temp = sorted(test_tup)
    res = tuple(temp[:K] + temp[-K:])
    # res=tuple(temp[0:k]+temp[-k:])
    # printing result 
    print("The extracted values : " + str(res)) 

test_tup = (5, 20, 3, 7, 6, 8)
k=2
maxi_min(test_tup,k)