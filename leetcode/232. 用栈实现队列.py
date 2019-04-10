class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        _temp_stack = []
        while len(self._stack) > 0:
            _temp_stack.append(self._stack.pop())
        v = _temp_stack.pop()
        while len(_temp_stack) > 0:
            self._stack.append(_temp_stack.pop())
        return v

    def peek(self) -> int:
        """
        Get the front element.
        """
        _temp_stack = []
        while len(self._stack) > 0:
            _temp_stack.append(self._stack.pop())
        v = _temp_stack[-1]
        while len(_temp_stack) > 0:
            self._stack.append(_temp_stack.pop())
        return v

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._stack) == 0
