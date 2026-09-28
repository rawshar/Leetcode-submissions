class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l=len(nums)
        pre_nums=[1]*(l+1)
        #post_nums=[1]*(l+1)
        right=1
        for i in range(l):#0,1,2,3
           
            pre_nums[i+1]=pre_nums[i]*nums[i]
        for i in range(l-1,-1,-1):
            pre_nums[i]=pre_nums[i]*right
            right*=nums[i]
            
        return pre_nums[:l]