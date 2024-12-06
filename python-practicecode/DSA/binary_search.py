def binary_search(list,target):
    left,right=0,len(list)-1
    while left <= right:
        # print("left:",left,"right:",right)    
        mid=(left+right)//2
        # print("mid:",mid)
        if list[mid]==target:
            return mid
        elif(list[mid]<target):
            left=mid+1
        else:
            right=mid-1
    return -1        

# print(binary_search([1,2,3,4,5],3))
print(binary_search([1,2,3,4,5],2)) 
# print(binary_search([10,20,30,40,50],80))


