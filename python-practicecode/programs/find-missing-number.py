list1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]

def missingnum(list1):
    result=set(range(min(list1),max(list1)+1))- set(list1)
    print (result)
    # print(type(result))
missingnum(list1)

 