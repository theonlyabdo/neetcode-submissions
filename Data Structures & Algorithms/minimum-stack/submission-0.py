class MinStack:

    def __init__(self):
        self.st = []
        self.smin = []
        #self.n = 0
        #self.minimum = float("inf")
        

    def push(self, val: int) -> None:
        self.st.append(val)
        #self.n += 1
        val = min (val, self.smin[-1] if self.smin else val)
        self.smin.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.smin.pop()
        #self.n -= 1

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.smin[-1]
        
