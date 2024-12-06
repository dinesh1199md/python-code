

# claimstairs if n=2 there is a 2 way to claim stairs ---- we can go 1 step or 2 steps only
'''1 and 1 steps 
   or only 2 steps so --> answes is 2 ways
'''

# @cache 
def claimbStairs(n):
    if n==1: return 1
    if n==2: return 2
    two_back=1
    one_back=2
    for i in range(2,n):
        nxt_num= two_back+one_back
        two_back= one_back
        one_back=nxt_num
    return one_back


print(claimbStairs(3))    