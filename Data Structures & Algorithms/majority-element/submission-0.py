from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)/2
        count=Counter(nums)
        for key,value in count.items():
            if value >l:
                return key

        