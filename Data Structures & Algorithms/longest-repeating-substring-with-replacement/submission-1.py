"""
You get a string 

if the character is not the same then you add to a que 
if the len of of the que is greater than k you deque the character and shorten the window, you shorten it till you reach the point of one from the que is same 
and you start again moving towards the right 

we need to check before returning as well

ABABBA
how to make sure we are counting the most occuring 
we need to use the counter 

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        max_freq = 0
        res = 0
        l = 0
        for r in range(0,len(s)):
            if s[r] in hmap:
                curr_freq = hmap[s[r]]+1
                hmap[s[r]]=curr_freq
            else:
                curr_freq = 1
                hmap[s[r]]=curr_freq
            max_freq = max(max_freq, curr_freq)
            if (r-l+1)-max_freq > k:
                hmap[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
        return res

        