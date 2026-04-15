from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        c=0
        for i in range(len(nums)):
            while count[c]==0:
                c+=1
            nums[i]=c
            count[c]-=1
        