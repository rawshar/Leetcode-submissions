from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hmap= {}
        for i, x in enumerate(nums):
            diff = target-x
            if diff in hmap:
                return [hmap[diff], i]
            else: 
                hmap[x]=i