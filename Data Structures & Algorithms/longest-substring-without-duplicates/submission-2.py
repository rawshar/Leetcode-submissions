class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp=0
        g=0
        queue=[]
        for rp in range(len(s)):
            while queue and s[rp] in queue:
                queue.pop(0)
                lp+=1
            queue.append(s[rp])
            g=max(g,(rp-lp+1))



        return g
        