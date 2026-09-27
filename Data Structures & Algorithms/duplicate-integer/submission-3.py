class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>1:
            nums = sorted(nums) # nlogn
            for i in range(len(nums)-1): #n
                if nums[i] == nums[i+1]:
                    return True
        return False