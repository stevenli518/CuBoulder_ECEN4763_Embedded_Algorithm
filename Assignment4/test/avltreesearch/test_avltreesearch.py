"""Test AVL tree search implementation."""


import unittest
import logging
import sys
from structures.avltree import avltree
from search.avltreesearch import avlsearch


class AVLstreeSearchTest(unittest.TestCase):
    """Class BSTree_SearchTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.btree = avltree.AVLTree()
        self.btree.insert(51)
        self.btree.insert(31)
        self.btree.insert(21)
        self.btree.insert(41)
        self.btree.insert(71)
        self.btree.insert(61)
        self.btree.insert(81)

        self.bst_search = avlsearch.AVLTreeSearch(self.btree.root)

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("AVLTree_SearchTestLog")

    def test_avl_tree_search_constructor(self):
        """1.Test avl constructor."""
        self.assertEqual(self.bst_search.tree.value, 51)

    def test_avl_tree_search_add_tree(self):
        """2.Test avl add_tree function."""
        self.bst_search.add_tree(self.btree.root)
        self.assertEqual(self.bst_search.tree.value, 51)

    def test_avl_tree_search_search_empty(self):
        """3.Test avl search_tree function in an empty tree."""
        self.bst_search.add_tree(None)
        self.assertEqual(self.bst_search.search(51), [None, 0])

    def test_avl_tree_search_search_root(self):
        """4.Test avl search_tree function at root."""
        self.assertEqual([51, 0], self.bst_search.search(51))

    def test_avl_tree_search_search_level1_left(self):
        """5.Test avl search_tree function at level 1 left."""
        self.assertEqual([31, 1], self.bst_search.search(31))

    def test_avl_tree_search_search_level2_left(self):
        """6.Test avl search_tree function at level 2 left."""
        self.assertEqual([21, 2], self.bst_search.search(21))

    def test_avl_tree_search_search_level1_right(self):
        """7.Test avl search_tree function at level 1 right."""
        self.assertEqual(self.bst_search.search(71), [71, 1])

    def test_avl_tree_search_search_level2_right(self):
        """8.Test avl search_tree function at level 2 right."""
        self.assertEqual([81, 2], self.bst_search.search(81))

    def test_avl_tree_search_search_level2_left_2(self):
        """9.Test avl search_tree function at level 2 left_2."""
        self.assertEqual([41, 2], self.bst_search.search(41))

    def test_avl_tree_search_search_level2_right_2(self):
        """10.Test avl search_tree function at level 2 right_2."""
        self.assertEqual([61, 2], self.bst_search.search(61))

    def test_avl_tree_search_add_tree_2(self):
        """11.Test add_tree function_2."""
        self.bst_search.add_tree(self.btree.root.right)
        self.assertEqual(self.bst_search.tree.value, 71)

    def test_avl_tree_search_add_tree_3(self):
        """12.Test add_tree function_3."""
        self.bst_search.add_tree(self.btree.root.right.left)
        self.assertEqual(self.bst_search.tree.value, 61)

    def test_avl_tree_search_add_tree_4(self):
        """13.Test add_tree function_4."""
        self.bst_search.add_tree(self.btree.root.left.left)
        self.assertEqual(self.bst_search.tree.value, 21)

    def test_bs_tree_search_add_tree_5(self):
        """14.Test add_tree function_5."""
        self.bst_search.add_tree(self.btree.root.left.right)
        self.assertEqual(self.bst_search.tree.value, 41)
