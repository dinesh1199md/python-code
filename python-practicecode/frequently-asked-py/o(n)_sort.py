
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


def dutch_national_flag(arr):
    low, high = 0, len(arr) - 1
    i = 0
    
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
            print("zero",arr)
        elif arr[i] == 2:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
            print("two",arr)
        else:
            i += 1
            print("one",arr)
    return arr
 
# Test the function
input_array = [1, 0, 2, 1, 0]
output = dutch_national_flag(input_array)
print("Sorted Array:", output)

