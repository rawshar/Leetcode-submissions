class MinStack:

    def __init__(self):
        self.stack=[]
        self.decreasing=[float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.decreasing and self.decreasing[-1]>=val:
            self.decreasing.append(val)       

    def pop(self) -> None:
        curr = self.stack.pop()
        if self.decreasing[-1] == curr:
            self.decreasing.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.decreasing[-1]
        
