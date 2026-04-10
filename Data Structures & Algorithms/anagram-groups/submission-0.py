from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for str in strs:
            count=[0]*26
            for c in str:
                count[ord(c)-ord('a')]+=1
            hmap[(tuple(count))].append(str)
        
        return list(hmap.values())



        