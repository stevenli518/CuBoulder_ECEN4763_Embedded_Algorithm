"""This Queue Module can be used to modularize the queue class."""


class Queue:
    """Class represents the queue algorithm data structure."""

    def __init__(self, maxsize):
        """Construct a new instance."""
        self.queue = []
        self.maxsize = maxsize

    def isempty(self):
        """Return TRUE if the queue is empty and FALSE if it is not."""
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, my_queue):
        """Add an element to the queue."""
        if len(self.queue) >= self.maxsize:
            return False
        lst = self.queue
        lst.append(my_queue)
        return my_queue

    def dequeue(self):
        """Remove the first element added to the queue."""
        if self.isempty():
            return False
        de_val = self.queue[0]
        self.queue = self.queue[1:]
        return de_val

    def queue_size(self):
        """Return the size of the queue."""
        return len(self.queue)

    def empty(self):
        """Empty the entire queue."""
        self.queue = []


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'
