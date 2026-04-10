from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[-x for x in count.values()]
        #print(heap)
        heapq.heapify(heap)

        interval=0
        while heap:
            temp=[]
            for i in range(n+1):
                if heap:
                    curr=heapq.heappop(heap)
                    if curr+1<0:
                        temp.append(curr+1)
                interval+=1
                if not temp and not heap:
                    break
                
            for val in temp:
                heapq.heappush(heap,val)
        return interval








        