import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            pebble1=-heapq.heappop(stones)
            pebble2=-heapq.heappop(stones)
            if pebble1==pebble2:
                continue
            heapq.heappush(stones,-abs(pebble1-pebble2))
                
        return -stones[0] if len(stones)>0 else 0
        