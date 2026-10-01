'''

'''
class Solution:
    def isValid(self, s: str) -> bool:
        open_b = ['(','{','[']
        hmap = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in open_b:
                stack.append(i)
            else:
                if stack:
                    if hmap[stack[-1]] == i:
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        return True if not stack else False

        