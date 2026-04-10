from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cyle=n+1
        freq=Counter(tasks)
        maxHeap=[-x for x in freq.values()]
        heapq.heapify(maxHeap)#[-3,-3]
        time=0

        while maxHeap:
            temp=[]
            for i in range(cyle):
                if maxHeap:
                    curr=heapq.heappop(maxHeap)
                    if curr+1<0:
                        temp.append(curr+1)
                time+=1
                if not(maxHeap) and not(temp):
                    break
                
            for val in temp:
                heapq.heappush(maxHeap,val)

        return time

                

        