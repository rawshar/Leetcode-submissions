"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
the problem is same as merge intervals but instead of merging 
I need to count where I would be merging or how many times I will be merging
merge interval problem it is
sort by the start time now 
if the start time is less than the prev end time we need to add a meeting room 
[(0,40),(5,10),(15,20)]
works for the above
but what if we add a 
[(1,5),(5,10),(10,15),(15,20)]

'''
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap=[]
        mr=0
        
        intervals.sort(key= lambda x:x.start)
        for i in intervals:
            if heap and i.start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,i.end)
        return len(heap)
        