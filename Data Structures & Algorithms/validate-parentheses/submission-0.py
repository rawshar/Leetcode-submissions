'''
will be using stack 
if we get ({[  then add to stack 
if we get this then pop from stack    ] } )
at the end if stack is not empty then false
if the value doesn't match then false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        hmap={'(':')','[':']','{':'}'}
        input=hmap.keys()
        stack=[]
        for i in s: 
            if i in input:
                stack.append(i)
            else:
                if stack:
                    if hmap[stack[-1]]!=i:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return False if len(stack)>0  else True
