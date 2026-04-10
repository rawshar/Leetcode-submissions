"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_list=[]
        for i in intervals:
            intervals_list.append((i.start,i.end))
        intervals_list.sort(key=lambda x:x[0])
        print(intervals_list)
        
        

        for i in range(1,len(intervals_list)):
            if intervals_list[i][0]<intervals_list[i-1][1]:
                return False
            

        return True 
