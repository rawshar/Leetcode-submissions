'''
move in one direction for a pointer 
the other one stay fixed ( so window expand)
condition: the extra character used should not be more than k
shrink logic to fix the window if the condition break

<we don't know what will come inside the window, so we create a counter>
1. counter will store the requency of each character
and will maintain max frequency 
as we get new character will check the value of max frequency 
2. instead of a counter for k will check if r-l+1 - maxFrequency is greater than k (condition)
3. if that is the case will move the l and remove the extra character for the maxFrequency
4. get the result for the final output as res
< problem I faced was that I was stuck at the change of character on A to B for Ex2 > but this take care of it 

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        counter={}
        res=0
        maxFreq=0
        for r in range(len(s)):
            counter[s[r]]=counter.get(s[r],0)+1
            maxFreq=max(maxFreq,counter[s[r]])

            while (r-l+1)-maxFreq>k:
                counter[s[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res

        