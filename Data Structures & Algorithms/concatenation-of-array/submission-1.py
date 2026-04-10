class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        final=[0]*(2*n)
        for i in range(n):
            final[i]=final[i+n]=nums[i]
        return final

        