'''
Get the list of tuple having distance and time 
then sort it out
start from the distance farthest from the target
if a car is ahead and time taken is more than this car ( so this car will slow)
No need to keep it in the stack remove it 
if both the cars are reaching in same time remove the prev one
check only the prev one in stack 
and at first I kept the if condition change it to while the stack is not empty 
return the len of stack
'''

"""
second approach change the direction 
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time =[(position[i], (target-position[i])/speed[i]) for i in range(len(position))]
        time.sort(reverse=True)
        stack=[]
        for i,t in time: 
            if not stack or  t>stack[-1]:
                stack.append(t)
        return len(stack)
                
        