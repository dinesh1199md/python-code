def trap(height):
    if not height:
        return 0
    ans=0
    l=0
    r=len(height)-1
    maxl=height[l]
    maxr=height[r]
    while l<r:
        if maxl<maxr:
            ans+=maxl-height[l]
            l+=1
            if maxl<height[l]:
                maxl=height[l]
        else:
            ans+=maxr-height[r]
            r-=1
            if maxr<height[r]:
                maxr=height[r]
    return ans



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

# https://leetcode.com/problems/trapping-rain-water/