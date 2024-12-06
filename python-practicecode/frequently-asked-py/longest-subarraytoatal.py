
def max_array(l):
    curr_sum=0
    max_sum=0
    for num in l:
        curr_sum+=num
        if curr_sum<0:
            curr_sum=0
        max_sum=max(max_sum,curr_sum)  

    return max_sum      

print(max_array([-0,-1,-5,-2,-3,-14]))
