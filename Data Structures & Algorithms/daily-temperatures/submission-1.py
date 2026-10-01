"""
warmer meaning higher value

"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        l=len(temperatures)
        answer = [0]*l
        stack = []
        for i in range(0,l):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                old_temp_index = stack.pop()
                answer[old_temp_index]=i-old_temp_index    
            stack.append(i)
        return answer

        