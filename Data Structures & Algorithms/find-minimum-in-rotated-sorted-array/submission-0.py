'''
find the sorted array from half and move towards it 
[3,4,5,1,2]
when I get in the middle if I find that the mid is greater that right means 
the left side of the array is sorted time to move on the right 
there will be the mininum number
it will make sense on larger array
[4,5,6,7,0,1,2] if mid > rp then it mean right side is not sorted well
[5,6,7,0,1,2,4] if mid < rp means the right side is sorted but not the left side
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp=0
        rp=len(nums)-1
        while lp<rp:
            mid=lp+(rp-lp)//2
            
            if nums[mid]>nums[rp]:
                lp=mid+1 
            else:
                rp=mid
        return nums[rp]
        