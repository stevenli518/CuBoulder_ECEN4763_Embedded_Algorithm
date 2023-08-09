"""test xor linked list implementation."""

# pylint: disable = R0904
import unittest
import logging
import sys
from structures.linkedlist import linkedlist


class XORListTest(unittest.TestCase):
    """Class Xor List."""

    def setUp(self):
        """Setup."""
        debug = True
        self.linkedlist = linkedlist.XORList()
        self.linkedlist.insert_begin(10)
        self.linkedlist.insert_begin(9)
        self.linkedlist.insert_begin(8)
        self.linkedlist.insert_begin(7)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("LinkedListTestLog")

    def test_linkedlist_insert(self):
        """1.Test insert at the beginnign."""
        self.linkedlist.insert_begin(6)
        self.linkedlist.printxorlist()

    def test_linkedlist_length(self):
        """2.Test length function."""
        self.assertEqual(self.linkedlist.length(), 4)

    def test_linkedlist_find(self):
        """3.Test find function."""
        self.assertEqual(self.linkedlist.find(10), True)

    def test_linkedlist_insert_before(self):
        """4.Test insert_before."""
        self.linkedlist.insert_before(9, 666)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_after(self):
        """5.Test insert_after."""
        self.linkedlist.insert_after(9, 666)
        self.linkedlist.insert_after(8, 555)
        self.linkedlist.insert_after(7, 444)
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_head(self):
        """5.Test: delete head"""
        self.linkedlist.delete_head()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_two_node(self):
        """6.Test: delete list with two nodes"""
        self.linkedlist.delete_head()
        self.linkedlist.delete_head()
        self.linkedlist.delete_head()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_single_node(self):
        """7.Test: delete list with one nodes"""
        self.linkedlist.delete_head()
        self.linkedlist.delete_head()
        self.linkedlist.delete_head()
        self.linkedlist.delete_head()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_tail(self):
        """8.Test: delete tail"""
        self.linkedlist.delete_tail()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete__tail_two_node(self):
        """9.Test: delete list with two nodes"""
        self.linkedlist.delete_tail()
        self.linkedlist.delete_tail()
        self.linkedlist.delete_tail()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_tail_single_node(self):
        """10.Test: delete list with one nodes"""
        self.linkedlist.delete_tail()
        self.linkedlist.delete_tail()
        self.linkedlist.delete_tail()
        self.linkedlist.delete_tail()
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_value(self):
        """11.Test: delete value from the list"""
        self.linkedlist.delete_node(8)
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_value_repeated(self):
        """12.Test: delete repeated value from the list"""
        self.linkedlist.delete_node(8)
        self.linkedlist.delete_node(8)
        self.linkedlist.printxorlist()

    def test_linkedlist_empty_list(self):
        """13.Test: empty whole list"""
        self.linkedlist.empty_list()
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_repeated_before(self):
        """14.Test insert_repeated_before."""
        self.linkedlist.insert_before(9, 666)
        self.linkedlist.insert_before(9, 666)
        self.linkedlist.printxorlist()

    def test_linkedlist_space_complexity(self):
        """15.Test space complexity."""
        self.assertEqual(linkedlist.get_space_complexity(), "O(n)")

    def test_linkedlist_time_complexity(self):
        """16.Test time complexity."""
        self.assertEqual(linkedlist.get_time_complexity(), "O(n)")

    def test_linkedlist_get_tail(self):
        """17.Test get tail."""
        temp = self.linkedlist.get_tail()
        self.assertEqual(temp.value, 10)

    def test_linkedlist_insert_beginning_repeated(self):
        """18.Test insert repeated value at beginning."""
        self.linkedlist.insert_begin(8)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_end_repeated(self):
        """19.Test insert repeated value at bend."""
        self.linkedlist.insert_end(8)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_end_no_head(self):
        """20.Test insert value at end when the list is empty."""
        self.linkedlist.empty_list()
        self.linkedlist.insert_end(666)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_before_empty(self):
        """21.Test insert value before when the list is empty."""
        self.linkedlist.empty_list()
        self.linkedlist.insert_before(8, 666)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_before_head(self):
        """22.Test insert value before head."""
        self.linkedlist.insert_before(7, 666)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_after_empty(self):
        """23.Test insert value after when the list is empty."""
        self.linkedlist.empty_list()
        self.linkedlist.insert_after(8, 666)
        self.linkedlist.printxorlist()

    def test_linkedlist_insert_after_repeated(self):
        """24.Test insert after a repeated value."""
        self.linkedlist.insert_after(8, 8)
        self.linkedlist.printxorlist()

    def test_linkedlist_find_length_empty_list(self):
        """25.Test find the length of an empty list."""
        self.linkedlist.empty_list()
        self.assertEqual(self.linkedlist.length(), 0)

    def test_linkedlist_delete_head_empty_list(self):
        """26.Test delete head of an empty list."""
        self.linkedlist.empty_list()
        self.linkedlist.delete_head()

    def test_linkedlist_delete_tail_empty_list(self):
        """27.Test delete head of an empty list."""
        self.linkedlist.empty_list()
        self.linkedlist.delete_tail()

    def test_linkedlist_delete_node_at_head(self):
        """28.Test delete head of an empty list."""
        self.linkedlist.delete_node(7)
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_node_at_tail(self):
        """29.Test delete tail of an empty list."""
        self.linkedlist.delete_node(10)
        self.linkedlist.printxorlist()

    def test_linkedlist_delete_empty_an_emptylist(self):
        """30.Test delete head of an empty list."""
        self.linkedlist.empty_list()
        self.linkedlist.printxorlist()
        self.linkedlist.empty_list()
