def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    # print("pivote",pivot)
    left = [x for x in arr if x < pivot]
    # print("left",left)
    middle = [x for x in arr if x == pivot]
    # print("middle",middle)
    right = [x for x in arr if x > pivot]
    # print("right",right)
    return quicksort(left) + middle + quicksort(right)

# Time complexity: O(n log n) on average, O(n^2) in worst case (when pivot is poorly chosen).

print(quicksort([2,3,6,7,4,1]))
