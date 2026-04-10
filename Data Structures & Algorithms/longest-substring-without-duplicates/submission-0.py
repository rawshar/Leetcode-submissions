'''
form a substring 
move to the right always 
I can use a queue in this case as well
I add the new character to the queue 
if a characeter is already in quque I will shrink the queue till that character is found 
and caluclate the max only when the duplicate character is there 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue=[]
        maxLen=0
        for char in s:
            if char  in queue:
                maxLen=max(maxLen,len(queue))
                val=queue.pop(0)
                while queue and val!=char:
                    val=queue.pop(0)
                queue.append(char)
            else:
                queue.append(char)


        return max(maxLen,len(queue))
        