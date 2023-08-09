"""This Stack Module can be used to modularize the qstack class."""


class Stack:
    """Class represents the queue algorithm data structure."""

    def __init__(self, maxsize):
        """Construct a new instance."""
        self.stack = []
        self.maxsize = maxsize

    def isempty(self):
        """Return TRUE if the stack is empty and FALSE if it is not."""
        if len(self.stack) == 0:
            return True
        return False

    def push(self, my_stack):
        """Add an element to the stack."""
        if len(self.stack) >= self.maxsize:
            return False
        self.stack.append(my_stack)
        return True

    def pop(self):
        """Remove the last element added to the stack."""
        if self.isempty():
            return False
        self.stack = self.stack[:len(self.stack)-1]
        return True

    def stack_size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def top_peek(self):
        """Return the value of the topmost element of the stack (last pushed)."""
        if self.isempty():
            return None
        return self.stack[len(self.stack)-1]

    def empty(self):
        """Empty the entire stack."""
        self.stack = []


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'
