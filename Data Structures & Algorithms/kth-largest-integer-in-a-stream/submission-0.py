import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k=k
        self._nums=nums
        heapq.heapify(self._nums)
        while len(self._nums)>self._k:
            heapq.heappop(self._nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self._nums,val)
        if len(self._nums)>self._k:
            heapq.heappop(self._nums)
        return self._nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)