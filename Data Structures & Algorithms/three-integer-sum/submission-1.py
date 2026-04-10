
'''
sort the nums
fix one and 2 pointer on another values
skipp the duplicate values for the movement of the pointers for 
1. first check the prev one
2. for lp check the next one
3. for rp check the prev one ( for all three one step at a time)
the lp and rp cannot meet at the same location because j!=k

**********in two pointer always check how we are incrementing ****** and when 


'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        l=len(nums)
        final=[]
        for i in range(l):

            if i>0 and nums[i]==nums[i-1]:
                continue

            lp=i+1
            rp=l-1
            while lp<rp:
                total = nums[i]+nums[lp]+nums[rp]
                if total==0:
                    final.append([nums[i],nums[lp],nums[rp]])
                    while lp<rp and nums[lp]==nums[lp+1]:
                        lp+=1
                    while lp<rp and nums[rp]==nums[rp-1]:
                        rp-=1
                    lp+=1
                    rp-=1


                elif total<0:
                    lp+=1
                else:
                    rp-=1
        return final

        