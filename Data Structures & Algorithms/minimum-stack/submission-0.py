class MinStack:

    def __init__(self):
        self._stack=[]
        self.min_val=float('inf')
        

    def push(self, val: int) -> None:
        if self.min_val > val:
            self.min_val=val
        self._stack.append(val)
        

    def pop(self) -> None:
        val=self._stack.pop()
        if val == self.min_val:
            if self._stack:
                self.min_val=min(self._stack)
            else:
                self.min_val=float('inf')
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()