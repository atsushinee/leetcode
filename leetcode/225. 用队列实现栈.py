class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._deque = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        _deque_len = len(self._deque)
        self._deque.append(x)
        for i in range(_deque_len):
            self._deque.append(self._deque.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._deque.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._deque[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._deque) == 0


if __name__ == '__main__':
    pass
