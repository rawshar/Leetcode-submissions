import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            raise ValueError("input empty")


        neg_stones = [-1 * stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            top1 = heapq.heappop(neg_stones)
            top2 = heapq.heappop(neg_stones)
            resolved = abs(top1 - top2) * -1
            heapq.heappush(neg_stones, resolved)
        return neg_stones[0] * -1