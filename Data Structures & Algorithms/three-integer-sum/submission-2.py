'''
sort the list 
keep one pointer stationary and move the other pointer towards one another
skipp the duplicates from the firt pointer by check the next one

if sum is =0 then append the value to list
for the two pointers using the if condition for the next one
as for the above one we will skipp the duplicate values
in two pointer always check how we are incrementing 

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        final=[]
        for i in range(l):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            lp = i+1
            rp = l-1
            while lp<rp:
                total= nums[i]+nums[lp]+nums[rp]
                if total== 0:
                    final.append([nums[i],nums[lp],nums[rp]])
                    
                    while lp<rp and nums[lp]== nums[lp+1]:
                        lp+=1
                    while lp<rp and nums[rp]==nums[rp-1]:
                        rp-=1
                    lp+=1
                    rp-=1
                elif total < 0:
                    lp+=1
                else:
                    rp-=1
                
        return final
                
        