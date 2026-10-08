import math
class Solution:
    def time_taken(self,piles,speed):
        h=0
        for i in piles :
            if i < speed:
                h+=1
            else:
                if i % speed >0:
                    h+=((i//speed)+1)
                else:
                    h+=(i//speed)
        return h
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_speed=max(piles)
        min_speed=1
        while min_speed<max_speed:
            curr_speed = min_speed+(max_speed-min_speed)//2
            curr_time = 0
            for i in piles:
                curr_time+=math.ceil(i/curr_speed)
            if curr_time<=h:
                max_speed=curr_speed
            else:
                min_speed=curr_speed+1
        return min_speed
        