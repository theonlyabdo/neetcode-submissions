class MinStack:

    def __init__(self):
        self.st = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        
        minimum = min(val, self.minstack[-1] if self.minstack else float('inf'))
        self.minstack.append(minimum)

    def pop(self) -> None:
        self.st.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
