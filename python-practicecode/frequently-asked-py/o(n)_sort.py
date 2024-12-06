
from dotenv import load_dotenv

def sort012(arr):
    low=0
    mid=0
    high=len(arr)-1

    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
             arr[high],arr[mid]=arr[mid],arr[high]
             high-=1
arr=[2,0,2,1,1,0]
sort012(arr)
print(arr)

# print(sorted(arr))

#steps
# [2,0,2,1,1,0] l=0,m=0,h=5
# [0,0,2,1,1,2] l=0,m=0,h=4
# [0,0,2,1,1,2] l=1,m=1,h=4
# [0,0,2,1,1,2] l=2,m=2,h=4
# [0,0,1,1,2,2] l=2,m=2,h=3
# [0,0,1,1,2,2] l=2,m=3,h=3
# [0,0,1,1,2,2] l=2,m=4,h=3



