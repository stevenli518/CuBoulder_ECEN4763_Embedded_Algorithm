"""This XOR linked list Module can be used to modularize the xor linked list class."""


import ctypes


class Node:
    """Class represents the Node class for xor linked list data structure."""

    def __init__(self, value):
        """Construct a new instance of Node."""
        self.value = value
        self.next = 0

    def get_address(self):
        """Get the address of a Node."""
        return self.next

    def get_value(self):
        """Get the value of a Node."""
        return self.value


def type_cast(i_d):
    """Cast the address of i_d so that we can use pointers in python."""
    return ctypes.cast(i_d, ctypes.py_object).value


def xor(xor_a, xor_b):
    """Return the xor of the inputs xor_a and xor_b."""
    return xor_a ^ xor_b


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'


def get_time_complexity():
    """Return the time complexity of find based on the number of elements in the list."""
    return "O(n)"


class XORList:
    """Class represents the XOR linked list data structure."""

    def __init__(self):
        """Construct a new instance of XORlist."""
        self.head = None
        self.tail = None
        self.array = []

    def get_head(self):
        """Get the head pointer of the linked list."""
        return self.head

    def get_tail(self):
        """Get the tail pointer of the linked list."""
        return self.tail

    def insert_begin(self, value):
        """Insert a node storing value at the beginning of the linked list."""
        # if self.find(value) is True:
        #     return
        in_node = Node(value)
        if self.head is None:
            self.head = in_node
            self.tail = in_node
        else:
            self.head.next = xor(self.head.next, id(in_node))
            in_node.next = xor(0, id(self.head))
            self.head = in_node
        self.array.append(in_node)

    def insert_end(self, value):
        """Insert a node stroing value at the end of the linked list."""
        # if self.find(value) is True:
        #     return
        in_node = Node(value)
        if self.head is None:
            self.head = in_node
            self.tail = in_node
        else:
            self.tail.next = xor(id(in_node), self.tail.next)
            in_node.next = id(self.tail)
            self.tail = in_node
        self.array.append(in_node)

    def insert_before(self, next_node, value):
        """Insert a node storing value before the specified value of next_node already existed."""
        if self.isempty() is True:
            return False
        # if self.find(value) is True:
        #     return True
        if next_node == self.head.value:
            self.insert_begin(value)
            return True
        in_node = Node(value)
        prev_node_ad = 0
        next_node_ad = 1
        curr = self.head
        while curr:
            next_node_ad = xor(prev_node_ad, curr.next)
            if curr.value == next_node:
                break
            prev_node_ad = id(curr)
            curr = type_cast(next_node_ad)
        prev_node = type_cast(prev_node_ad)
        prev_prev_ad = xor(prev_node.next, id(curr))
        prev_node.next = xor(prev_prev_ad, id(in_node))
        in_node.next = xor(prev_node_ad, id(curr))

        curr.next = xor(id(in_node), next_node_ad)

        self.array.append(in_node)
        return True

    def insert_after(self, prev_node, value):
        """Insert a node storing value after the specified value of prev_node already existed."""
        if self.isempty() is True:
            return False
        # if self.find(value) is True:
        #     return True
        if prev_node == self.head.value:
            self.insert_end(value)
            return True
        in_node = Node(value)
        prev_node_ad = 0
        next_node_ad = 1
        curr = self.head
        while curr:
            next_node_ad = xor(prev_node_ad, curr.next)
            if curr.value == prev_node:
                break
            prev_node_ad = id(curr)
            curr = type_cast(next_node_ad)
        curr.next = xor(prev_node_ad, id(in_node))
        next_node = type_cast(next_node_ad)
        next_next_ad = xor(next_node.next, id(curr))
        in_node.next = xor(id(curr), next_node_ad)
        next_node.next = xor(id(in_node), next_next_ad)
        self.array.append(in_node)
        return True

    def find(self, value):
        """Return true if value is in list and false if value is not in list."""
        if self.isempty() is True:
            return False
        prev_node_ad = 0
        temp = Node(None)
        temp = self.head
        next_node_ad = None
        while temp:
            if temp.value == value:
                return True
            next_node_ad = xor(prev_node_ad, temp.next)
            prev_node_ad = id(temp)
            if next_node_ad == 0:
                break
            temp = type_cast(next_node_ad)
        return False

    def length(self):
        """Return the lenght of the linked list, returns 0 if the list is empty."""
        if self.isempty() is True:
            return 0
        prev_node_ad = 0
        next_node_ad = 1
        temp = self.get_head()
        length = 0
        while temp is not None:
            length += 1
            next_node_ad = xor(prev_node_ad, temp.get_address())
            prev_node_ad = id(temp)
            if next_node_ad == 0:
                break
            temp = type_cast(next_node_ad)
        return length

    def printxorlist(self):
        """Print the values in the linked list."""
        if self.head is not None:
            prev_node_ad = 0
            next_node_ad = 1
            temp = self.get_head()
            print("\n")
            while temp:
                print(temp.get_value())
                next_node_ad = xor(prev_node_ad, temp.get_address())
                if next_node_ad == 0:
                    return
                prev_node_ad = id(temp)
                temp = type_cast(next_node_ad)

    def isempty(self):
        """Return true if the linked list is empty and false if the list is not empty."""
        if self.head is None:
            return True
        return False

    def delete_head(self):
        """Delete the head of the linked list."""
        if self.isempty() is True or self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if self.head.next == id(self.tail):
            self.head = self.tail
            self.head.next = 0
            self.tail.next = 0
            return
        temp = self.head
        if temp.next is not None:
            next_node = type_cast(temp.next)
            next_next_ad = xor(next_node.next, id(temp))
            next_node.next = xor(0, next_next_ad)
            self.head = next_node
            temp = None
            return
        # self.head = None

    def delete_tail(self):
        """Delete the tail of the linked list."""
        if self.isempty() is True or self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if self.head.next == id(self.tail):
            self.tail = self.head
            self.tail.next = 0
            self.head.next = 0
            return
        temp = self.tail
        prev_ad = xor(0, temp.next)
        prev_node = type_cast(prev_ad)
        prev_prev_ad = xor(prev_node.next, id(temp))
        prev_node.next = prev_prev_ad
        temp = None
        self.tail = prev_node

    def delete_node(self, value):
        """Delete the node containing value."""
        if self.isempty() is True or self.tail is None or self.find(value) is False:
            return
        if self.head.value == value:
            self.delete_head()
            return
        if self.tail.value == value:
            self.delete_tail()
            return
        prev_node_ad = 0
        next_node_ad = 1
        temp = self.get_head()
        while temp.value != value:
            next_node_ad = xor(prev_node_ad, temp.next)
            prev_node_ad = id(temp)
            temp = type_cast(next_node_ad)
        prev_node = type_cast(prev_node_ad)
        prev_prev_id = xor(prev_node.next, id(temp))
        next_node = type_cast(xor(prev_node_ad, temp.next))
        next_next_id = xor(next_node.next, id(temp))

        prev_node.next = xor(prev_prev_id, id(next_node))
        next_node.next = xor(next_next_id, prev_node_ad)
        return

    def empty_list(self):
        """Delete the entire linked list."""
        if self.isempty() is True:
            return
        while self.isempty() is not True:
            self.delete_head()
        return
