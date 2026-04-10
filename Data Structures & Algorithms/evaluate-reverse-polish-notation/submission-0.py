'''
take the floor in division ? 
whenever there is an operator the operands will be behing it 
after the operation put it back 
do it again till end 
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        stack=[]

        for i in tokens:
            if i in operators:
                op1=int(stack.pop())
                op2=int(stack.pop())
                if i == '+':
                    stack.append(op2+op1)
                elif i=='-':
                    stack.append(op2-op1)
                elif i=='/':
                    stack.append(int(op2/op1))
                else:
                    stack.append(op2*op1)
            else:
                stack.append(i)

        return int(stack[-1])
        