from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        count = Counter(nums)
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [ num for freq,num in heap]

        