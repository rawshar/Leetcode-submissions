from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1=Counter(s1)
        lp=0
        l1=len(s1)
        counter2=Counter()
        for rp in range(len(s2)):
            counter2[s2[rp]]=counter2.get(s2[rp],0)+1
            if rp-lp+1>l1:
                counter2[s2[lp]]-=1
                if counter2[s2[lp]]==0:
                    del counter2[s2[lp]]
                lp+=1
            if counter1==counter2:
                return True
        return False

        