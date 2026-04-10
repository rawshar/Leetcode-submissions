'''
1. use the two pointer patter moving towards one another
2. breaking condition is that the cannot be on same line
3. whichever is the min height among the two height will be incremented/decremented respectively
4. a variable with max area is returned
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        g=0
        lp=0
        rp=len(height)-1
        while lp<rp:
            curr=(rp-lp)*min(height[lp],height[rp])
            g=max(g,curr)
            if height[lp]<=height[rp]:
                lp+=1
            else:
                rp-=1

        return g
        