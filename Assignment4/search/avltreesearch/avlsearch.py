"""This AVLBST Search Module can be used to modularize the binary_search_tree class."""


def find_helper(node, value_to_find, steps=0):
    """Return True if a value is present in the tree and False if the value is not present."""
    if node is None:
        my_lst = [None, 0]
        return my_lst
    if value_to_find < node.value:
        steps += 1
        my_lst = find_helper(node.left, value_to_find, steps)
        return my_lst
    if value_to_find > node.value:
        steps += 1
        my_lst = find_helper(node.right, value_to_find, steps)
        return my_lst
    my_lst = [value_to_find, steps]
    return my_lst


class AVLTreeSearch:
    """Class represents the AVL binary tree search."""

    def __init__(self, bstree):
        """Initialize the class variable storing the tree to bstree."""
        self.tree = bstree

    def add_tree(self, bstree):
        """Set the class variable for the tree to bstree."""
        self.tree = bstree

    def search(self, value_to_find, steps=0):
        """Return the value if it is found or None if it is not."""
        # if self.tree is None:
        #     return None
        if self.tree is None:
            print("\n")
            print("YOOOOO")
        return find_helper(self.tree, value_to_find, steps)
