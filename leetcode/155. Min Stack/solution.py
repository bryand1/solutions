class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = [(-1, float('inf'))]

    def push(self, x: int) -> None:
        self.st.append((x, min(x, self.st[-1][1])))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][-1]
