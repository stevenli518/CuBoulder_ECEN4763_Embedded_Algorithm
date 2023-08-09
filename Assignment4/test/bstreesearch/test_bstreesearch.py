"""Test binary tree search implementation."""


import unittest
import logging
import sys
from structures.binary_search_tree import binary_search_tree
from search.bstreesearch import bstreesearch


class BstreeSearchTest(unittest.TestCase):
    """Class BSTree_SearchTest."""

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
        self.bst_search = bstreesearch.BSTreeSearch(self.btree)

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BTree_SearchTestLog")

    def test_bs_tree_search_constructor(self):
        """1.Test constructor."""
        self.assertEqual(self.bst_search.tree.value, 50)

    def test_bs_tree_search_add_tree(self):
        """2.Test add_tree function."""
        self.bst_search.add_tree(self.btree.left)
        self.assertEqual(self.bst_search.tree.value, 30)

    def test_bs_tree_search_search_empty(self):
        """3.Test search_tree function in an empty tree."""
        self.bst_search.add_tree(None)
        self.assertEqual(self.bst_search.search(30), None)

    def test_bs_tree_search_search_root(self):
        """4.Test search_tree function at root."""
        self.assertEqual(self.bst_search.search(50), [50, 0])

    def test_bs_tree_search_search_level1_left(self):
        """5.Test search_tree function at level 1 left."""
        self.assertEqual(self.bst_search.search(30), [30, 1])

    def test_bs_tree_search_search_level2_left(self):
        """6.Test search_tree function at level 2 left."""
        self.assertEqual(self.bst_search.search(20), [20, 2])

    def test_bs_tree_search_search_level1_right(self):
        """7.Test search_tree function at level 1 right."""
        self.assertEqual(self.bst_search.search(70), [70, 1])

    def test_bs_tree_search_search_level2_right(self):
        """8.Test search_tree function at level 2 right."""
        self.assertEqual(self.bst_search.search(80), [80, 2])

    def test_bs_tree_search_search_level2_left_2(self):
        """9.Test search_tree function at level 2 left_2."""
        self.assertEqual(self.bst_search.search(40), [40, 2])

    def test_bs_tree_search_search_level2_right_2(self):
        """10.Test search_tree function at level 2 right_2."""
        self.assertEqual(self.bst_search.search(60), [60, 2])

    def test_bs_tree_search_add_tree_2(self):
        """11.Test add_tree function_2."""
        self.bst_search.add_tree(self.btree.right)
        self.assertEqual(self.bst_search.tree.value, 70)

    def test_bs_tree_search_add_tree_3(self):
        """12.Test add_tree function_3."""
        self.bst_search.add_tree(self.btree.right.left)
        self.assertEqual(self.bst_search.tree.value, 60)

    def test_bs_tree_search_add_tree_4(self):
        """13.Test add_tree function_4."""
        self.bst_search.add_tree(self.btree.left.left)
        self.assertEqual(self.bst_search.tree.value, 20)

    def test_bs_tree_search_add_tree_5(self):
        """14.Test add_tree function_5."""
        self.bst_search.add_tree(self.btree.left.right)
        self.assertEqual(self.bst_search.tree.value, 40)
