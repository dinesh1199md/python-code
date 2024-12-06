def right_rotate(arr, d):
    print(arr[-d % len(arr):])
    print(arr[:-d % len(arr)])
    return arr[-d % len(arr):] + arr[:-d % len(arr)]
arr = [1, 2, 3, 4, 5]
print(right_rotate(arr, 2))


# 12345
# 51234
# 45123

def left_rotate(arr, d):
    return arr[d % len(arr):] + arr[:d % len(arr)]
arr = [1, 2, 3, 4, 5]
print(left_rotate(arr, 2))