from collections import Counter, defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        for key,freq in count.items():
            heapq.heappush(heap,(freq,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [ _ for freq,_ in heap ]

        
        