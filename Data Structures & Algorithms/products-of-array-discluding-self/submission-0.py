class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        left=[1]*l
        right=1
        for i in range(1,len(left)):
            left[i]=nums[i-1]*left[i-1]
        #running right product
        for i in range(l-1,-1,-1):
            left[i]=left[i]*right
            right=right*nums[i]
        return left

        