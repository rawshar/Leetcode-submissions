'''
Using 2 pointer
1. two pointers moves towards each other
2. break condition to stop searching not to use the same element again(not having same value)
3.return the indices of two number incremented by one
no extra space o(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lp=0
        rp=len(numbers)-1
        while lp<rp:
            curr=numbers[lp]+numbers[rp]
            if curr == target:
                return [lp+1,rp+1]
            elif curr>target:
                rp-=1
            else:
                lp+=1