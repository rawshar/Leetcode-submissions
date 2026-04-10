'''
Cannot be done using two pointer or window
as when we shrink the window we move the left pointer but here we need to check
the value one back from the rp at distance 1 or more

so use stack:
1. create an empty stack(will be adding index instead of values)
2. if stack is empty or stack[-1]>curr -> add to stack
3. if stack[-1]<curr -> empty and add the diff to answer till stack is empty or stack[-1]>curr
4. repeat till the for loop is done
5. loop through stack and put 0 to all index in the stack

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[0]*len(temperatures)
        for x in range(len(temperatures)):
            while stack and (temperatures[stack[-1]]<temperatures[x]):
                index=stack.pop()
                answer[index]=x-index
            stack.append(x)
        return answer
        