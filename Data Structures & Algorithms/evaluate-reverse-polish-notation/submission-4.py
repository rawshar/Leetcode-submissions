import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=set(['-','+','/','*'])
        operand=[]
        for i in tokens:
            if i in operators:
                operand1=operand.pop()
                operand2=operand.pop()
                if i =='-':
                    operand.append(operand2-operand1)
                    print(operand1-operand2,operand1,operand2)
                elif i =='/':
                    val=math.floor(operand2/operand1) if operand2/operand1 >0 else math.ceil(operand2/operand1)
                    operand.append(val)
                elif i =='+':
                    operand.append(operand2+operand1)
                else:
                    operand.append(operand2*operand1)


            else:
                operand.append(int(i))
            print(operand)
        return operand[0]
        