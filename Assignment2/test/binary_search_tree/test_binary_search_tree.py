"""test binary search tree implementation."""


import unittest
import logging
import sys
from structures.binary_search_tree import binary_search_tree


class BSTreeTest(unittest.TestCase):
    """Class BSTreeTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.btree = binary_search_tree.Node(50)
        self.btree.insert(30)
        self.btree.insert(20)
        self.btree.insert(40)
        self.btree.insert(70)
        self.btree.insert(60)
        self.btree.insert(80)

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BTreeTestLog")

    def test_bs_tree_insertion(self):
        """1.Test insertion."""
        self.assertEqual(self.btree.insert(10), True)
        print("\n")
        self.btree.printbtree()

    def test_bs_tree_insertion_repeated(self):
        """2.Test insertion-repeated values."""
        self.assertEqual(self.btree.insert(20), True)
        print("\n")
        self.btree.printbtree()

    def test_bs_tree_deletion_left(self):
        """3.Test deletion-leaf."""
        print("\n")
        self.btree.delete_node(20)
        self.btree.printbtree()

    def test_bs_tree_deletion_right(self):
        """4.Test deletion-leaf."""
        print("\n")
        self.btree.delete_node(80)
        self.btree.printbtree()

    def test_bs_tree_deletion_onechild(self):
        """5.Test deletion-onechild."""
        print("\n")
        self.btree.delete_node(20)
        self.btree.delete_node(30)
        self.btree.printbtree()

    def test_bs_tree_deletion_twochild(self):
        """6.Test deletion-twochild."""
        print("\n")
        self.btree.delete_node(20)
        self.btree.delete_node(30)
        self.btree.delete_node(50)
        self.btree.printbtree()

    def test_bs_tree_deletion_repeated_left(self):
        """7.Test deletion-repeated"""
        self.btree.delete_node(20)
        self.assertEqual(self.btree.delete_node(20), False)

    def test_bs_tree_deletion_repeated_right(self):
        """8.Test deletion-repeated"""
        self.btree.delete_node(80)
        self.assertEqual(self.btree.delete_node(80), False)

    def test_bs_tree_value_present1(self):
        """9.Test: Check if a value is present in the tree or not."""
        self.assertEqual(self.btree.findval(20), True)

    def test_bs_tree_value_present2(self):
        """10.Test: Check if a value is present in the tree or not."""
        self.assertEqual(self.btree.findval(80), True)

    def test_bs_tree_height(self):
        """11.Test: Check the maximum height of the tree."""
        self.assertEqual(self.btree.depth(self.btree), 2)

    def test_test_tree_space_complexity(self):
        """12.Test: Space time of the BST"""
        self.assertEqual(binary_search_tree.get_space_complexity(), 'O(n)')

    def test_test_tree_time_complexity(self):
        """13.Test: time complexity of the BST"""
        self.assertEqual(binary_search_tree.get_time_complexity(), 'O(logn)')

    def test_bs_tree_print(self):
        """14.Test: Print BST."""
        print("\n")
        self.btree.printbtree()
