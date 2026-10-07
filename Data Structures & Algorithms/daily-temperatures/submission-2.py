class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        l=len(temperatures)
        final = [0]*l
        for i in range(l):
            
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev = stack.pop()
                final[prev]=i-prev
            stack.append(i)
        return final
        