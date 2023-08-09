"""This AVL binary search tree Module can be used to modularize the binary_search_tree class."""


# pylint: disable = R0911
# Citation: Adapted from GeeksforGeeks
class Node:
    """Class represents the Node class for AVL BST data structure."""

    def __init__(self, value, right=None, left=None, height=None):
        """Construct a new instance of Node."""
        self.value = value
        self.left = left
        self.right = right
        self.height = height

    def get_height(self):
        """Return the height variable of the node."""
        return self.height

    def set_height(self, height):
        """Set the height variable of the node to height."""
        self.height = height


def height_helper(node):
    """Get Height helper."""
    if node is None:
        return 0
    return node.get_height()


def balance(node):
    """Get the balence factor."""
    if node is None:
        return 0
    return height_helper(node.left) - height_helper(node.right)


def leftrotate(node):
    """Left Rotation function."""
    right_c = node.right
    right_left = right_c.left
    right_c.left = node
    node.right = right_left
    node.set_height(1 + max(height_helper(node.left), height_helper(node.right)))
    right_c.set_height(1 + max(height_helper(right_c.left), height_helper(right_c.right)))
    return right_c


def rightrotate(node):
    """Right Rotation function."""
    left_c = node.left
    left_right = left_c.right
    left_c.right = node
    node.left = left_right
    node.set_height(1 + max(height_helper(node.left), height_helper(node.right)))
    left_c.set_height(1 + max(height_helper(left_c.left), height_helper(left_c.right)))
    return left_c


def insert_helper(node, val):
    """Insert node helper."""
    if node is None:
        return Node(val, None, None, 1)
    if val < node.value:
        node.left = insert_helper(node.left, val)
    if val > node.value:
        node.right = insert_helper(node.right, val)

    node.set_height(1 + max(height_helper(node.left), height_helper(node.right)))

    balance_height = balance(node)
    if balance_height > 1:
        if val < node.left.value:
            return rightrotate(node)
        node.left = leftrotate(node.left)
        return rightrotate(node)

    if balance_height < -1:
        if val > node.right.value:
            return leftrotate(node)
        node.right = rightrotate(node.right)
        return leftrotate(node)

    return node


def delete_helper(node, val):
    """Delete a node helper."""
    if val < node.value:
        node.left = delete_helper(node.left, val)
    elif val > node.value:
        node.right = delete_helper(node.right, val)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = node.right
        min_val = temp.value
        while temp.left is not None:
            temp = temp.left
            min_val = temp.value
        node.value = min_val
        node.right = delete_helper(node.right, min_val)

    node.height = 1 + max(height_helper(node.left), height_helper(node.right))

    balance_height = balance(node)
    if balance_height > 1:
        if balance(node.left) >= 0:
            return rightrotate(node)
        node.left = leftrotate(node.left)
        return rightrotate(node)
    if balance_height < -1:
        if balance(node.right) <= 0:
            return leftrotate(node)
        node.right = rightrotate(node.right)
        return leftrotate(node)

    return node


def print_helper(node):
    """Print helper."""
    if node.left:
        print_helper(node.left)
    print(node.value)
    if node.right:
        print_helper(node.right)


def find_helper(node, val):
    """Return True if a value is present in the tree and False if the value is not present."""
    if node.value == val:
        return True
    if val < node.value and node.left:
        return find_helper(node.left, val)
    if val > node.value and node.right:
        return find_helper(node.right, val)
    return False


class AVLTree:
    """Class represents the AVL Tree class."""

    def __init__(self):
        """Construct a new instance of AVLTree."""
        self.root = None

    def get_root(self):
        """Return the root of the tree."""
        return self.root

    def remove(self, val):
        """Remove a value from the tree and returns the value removed or None if not in the tree."""
        if self.root is None:
            return False
        if find_helper(self.root, val) is False:
            return False
        self.root = delete_helper(self.root, val)
        return True

    def insert(self, val):
        """Insert a value into the tree and returns True if successful, False otherwise."""
        self.root = insert_helper(self.root, val)
        return True

    def height(self):
        """Return the height of the tree."""
        return self.root.get_height()

    def min(self):
        """Return the minimum value present in the tree."""
        node = self.get_root()
        while node.left:
            node = node.left
        return node.value

    def max(self):
        """Return the maximum value present in the tree."""
        node = self.get_root()
        while node.right:
            node = node.right
        return node.value

    def is_empty(self):
        """Return True if no root is present, False otherwise."""
        if self.root is None:
            return True
        return False


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'


def get_time_complexity():
    """Return the time complexity of insertion into the data structure."""
    return 'O(logn)'
