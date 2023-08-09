"""This BST Search Module can be used to modularize the binary_search_tree class."""


class BSTreeSearch:
    """Class represents the binary tree search."""

    def __init__(self, bstree):
        """Initialize the class variable storing the tree to bstree."""
        self.tree = bstree

    def add_tree(self, bstree):
        """Set the class variable for the tree to bstree."""
        self.tree = bstree

    def search(self, value_to_find, steps=0):
        """Return the value if it is found or None if it is not."""
        if self.tree is None:
            return None
        if value_to_find < self.tree.value:
            self.add_tree(self.tree.left)
            steps += 1
            return self.search(value_to_find, steps)
        if value_to_find > self.tree.value:
            self.add_tree(self.tree.right)
            steps += 1
            return self.search(value_to_find, steps)
        return [value_to_find, steps]
