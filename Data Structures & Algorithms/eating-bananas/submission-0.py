'''
We need to find the optimal solution for the number of hours
should be minimum and then speed is good enough 

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp=1
        rp=max(piles)
        
        while lp<=rp:
            mid=lp+(rp-lp)//2
            time=0
            for i in piles:
                time+=math.ceil(i/mid)
            if time<=h:
                rp=mid-1
            else:
                lp=mid+1
        return lp
        