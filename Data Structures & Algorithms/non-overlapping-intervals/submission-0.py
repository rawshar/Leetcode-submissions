'''
[[1,2],[1,3],[2,3],[3,4]]
Merging it will be maximum number of intervals removed 
but for the minmum number of non overlapping intervals it will be different
we want the most interval to stay intact we will be removing the largest one and keeping the count more
merge interval will reduce the count
if we try to sort it by end time 
and if we use the end time as the start time for merge intervals
sorted
res=[]
for start, end in intervals:
    if not res or end<=res[-1][0]:
        res.append([star,end])
    else:
        continue

'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        there is no need for the res we just need to count
        replace res with count and where ever it was continue count+=1
        and create a variable with prevEnd 
        '''
        count=0
        prevEnd=-float('inf')
        intervals.sort(key=lambda x:x[1])
        for start, end in intervals:
            if  start>=prevEnd:
                prevEnd=end
            else:
                count+=1
        return count
        