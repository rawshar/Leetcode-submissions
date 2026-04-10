import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        heapq.heapify(heap)
        for p in points:
            heapq.heappush(heap,(-(p[0]*p[0]+p[1]*p[1]),p))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x[1] for x in heap ]