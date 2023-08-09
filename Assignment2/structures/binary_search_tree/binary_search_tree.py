"""This binary search tree(BST) Module can be used to modularize the binary_search_tree class."""


class Node:
    """Class represents the Node class for BST data structure."""

    def __init__(self, value):
        """Construct a new instance of Node."""
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert value into the the tree trying to maintain its balance as a binary tree."""
        if self.value == value:
            return True
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            self.left = Node(value)
            return True
        if self.right:
            return self.right.insert(value)
        self.right = Node(value)
        return True

    def findval(self, data):
        """Return True if a value is present in the tree and False if the value is not present."""
        if self.value == data or self.value is None:
            return True
        if data < self.value and self.left:
            return self.left.findval(data)
        if data > self.value and self.right:
            return self.right.findval(data)
        return False

    def depth(self, node):
        """Return the height of the binary tree from the root till the leaves."""
        if node is None:
            return -1
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        return max(left_depth, right_depth) + 1

    def printbtree(self):
        """Print the values in the tree."""
        if self.left:
            self.left.printbtree()
        print(self.value)
        if self.right:
            self.right.printbtree()

    def delete_node(self, key):
        """Delete a value from the tree. It returns False if there is no value to be deleted."""
        if self.findval(key) is False:
            return False
        if key < self.value:
            self.left = self.left.delete_node(key)
            return self
        if key > self.value:
            self.right = self.right.delete_node(key)
            return self
        if not self.right:
            return self.left
        if not self.left:
            return self.right
        temp = self.right
        min_val = temp.value
        while temp.left is not None:
            temp = temp.left
            min_val = temp.value
        self.value = min_val
        self.right = self.right.delete_node(min_val)
        return self


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'


def get_time_complexity():
    """Return the time complexity of findval based on the number of elements in the tree."""
    return 'O(logn)'
