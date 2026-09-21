class MinStack:

    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self._min:
            self._min.append(0)
        elif val < self.stack[self._min[-1]]:
            self._min.append(len(self.stack)-1)
        else:
            self._min.append(self._min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self._min[-1]]
