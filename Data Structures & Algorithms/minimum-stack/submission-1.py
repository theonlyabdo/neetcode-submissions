class MinStack:

    def __init__(self):
        self.st =[]
        self.minst = []
        self.minimum = float("inf")
        

    def push(self, val: int) -> None:
        self.st.append(val)
        #self.minimum = min (val, self.minimum)
        val = min (val, self.minst[-1] if self.minst else val)
        self.minst.append(val)

    def pop(self) -> None:
        self.st.pop()
        #self.minimum = min(self.st)
        self.minst.pop()
        
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]