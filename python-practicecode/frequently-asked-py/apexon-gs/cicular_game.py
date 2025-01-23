
def findTheWinner(n: int, k: int) -> int:
    circle=[i for i in range(1,n+1)]
    cur_inx=0

    while len(circle)!=1:
        remove_inx=(cur_inx+(k-1))%len(circle)
        circle.pop(remove_inx)
        cur_inx=remove_inx
    return circle[0]
print(findTheWinner(5,2))

# https://leetcode.com/problems/find-the-winner-of-the-circular-game/