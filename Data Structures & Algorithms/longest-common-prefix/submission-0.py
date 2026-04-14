class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]

        for i in range(1,len(strs)):
            curr=strs[i]
            min_length=min(len(res),len(curr))
            res=res[:min_length]
            curr=curr[:min_length]
            for j in range(min_length):
                if res[j]!=curr[j]:
                    res=res[:j]
                    break
            
            if len(res)==0:
                return ""
        return res
        
        