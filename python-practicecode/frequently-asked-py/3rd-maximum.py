
def thired_max(l):
    max=-1
    s_max=-1
    t_max=-1
    for num in l:
        if num>max:
            t_max=s_max
            s_max=max
            max=num
        elif(num>s_max and num<max):
            t_max=s_max
            s_max=num
        elif(num>t_max and num<s_max):
            t_max=num
    return t_max             
print(thired_max([2,1,3,4,8,9]))

