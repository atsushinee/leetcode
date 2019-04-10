class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._arr = []

    def push(self, x: int) -> None:
        if len(self._arr) == 0:
            self._arr.append(x)
            self._arr.append(x)
        else:
            top = self._arr[-1]
            self._arr.append(x)
            if top < x:
                self._arr.append(top)
            else:
                self._arr.append(x)

    def pop(self) -> None:
        self._arr.pop()
        self._arr.pop()

    def top(self) -> int:
        return self._arr[-2]

    def getMin(self) -> int:
        return self._arr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':

    minStack = MinStack()
    minStack.push(-2)
    print(minStack._arr)
    minStack.push(0)
    print(minStack._arr)
    minStack.push(-3)
    print(minStack._arr)
    # minStack.getMin()
    print(minStack.pop())
    print(minStack.pop())
    print(minStack.push(-1))
    print(minStack.getMin())

    # minStack.top()
    # minStack.getMin()
