import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        stack=[]

        for i in tokens:
            if i in operators:
                temp=0
                op1=int(stack.pop())
                op2=int(stack.pop())
                if i == '+':
                    temp=op2+op1
                elif i=='-':
                    temp=op2-op1
                elif i=='/':
                    temp=math.floor(op2/op1) if op2/op1 >0 else math.ceil(op2/op1)

                else:
                    temp=op2*op1
                stack.append(temp)
            else:
                stack.append(i)

        return int(stack[0])