"""test avl tree search implementation."""


import unittest
import logging
import sys
from structures.avltree import avltree


class AVLBstreeTest(unittest.TestCase):
    """Class BSTree_SearchTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.avltree = avltree.AVLTree()

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BTree_SearchTestLog")

    def test_insert(self):
        """1. Test AVLTree insert function."""
        self.avltree.insert(50)
        self.avltree.insert(30)
        self.avltree.insert(20)
        self.avltree.insert(40)
        self.avltree.insert(70)
        self.avltree.insert(60)
        self.avltree.insert(80)
        avltree.print_helper(self.avltree.get_root())

    def test_right_rotate(self):
        """2. Test right_totate."""
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        avltree.print_helper(self.avltree.get_root())

    def test_left_rotate(self):
        """3. Test left_totate."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        avltree.print_helper(self.avltree.get_root())

    def test_left_right_rotate(self):
        """4. Test left_right_totate."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)

    def test_right_left_rotate(self):
        """5. Test left_right_totate."""
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.assertEqual(self.avltree.insert(5), True)

    def test_remove_left_rotate(self):
        """6. Test left_rotate_remove."""
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.assertEqual(self.avltree.remove(1), True)
        self.assertEqual(self.avltree.remove(2), True)
        self.assertEqual(self.avltree.remove(3), True)
        self.assertEqual(self.avltree.remove(4), True)
        self.assertEqual(self.avltree.remove(5), True)
        self.assertEqual(self.avltree.remove(6), True)
        self.assertEqual(self.avltree.remove(7), True)
        avltree.print_helper(self.avltree.get_root())

    def test_remove_right_left_rotate(self):
        """7. Test right_leftremove."""
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.assertEqual(self.avltree.remove(7), True)
        self.assertEqual(self.avltree.remove(6), True)
        self.assertEqual(self.avltree.remove(5), True)
        self.assertEqual(self.avltree.remove(4), True)
        self.assertEqual(self.avltree.remove(3), True)
        self.assertEqual(self.avltree.remove(2), True)
        self.assertEqual(self.avltree.remove(1), True)

    def test_get_height(self):
        """8. Test get_height function."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.assertEqual(self.avltree.height(), 4)

    def test_get_min(self):
        """9. Test get_min function."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.assertEqual(self.avltree.min(), 1)

    def test_get_max(self):
        """10. Test get_max function."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.assertEqual(self.avltree.max(), 10)

    def test_is_empty(self):
        """11. Test is_empty()."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.assertEqual(self.avltree.is_empty(), False)

    def test_is_empty_2(self):
        """12. Test is_empty()."""
        self.assertEqual(self.avltree.is_empty(), True)

    def test_get_space_complexity(self):
        """13. Test get space complexity."""
        self.assertEqual(avltree.get_space_complexity(), 'O(n)')

    def test_get_time_complexity(self):
        """14. Test get time complexity."""
        self.assertEqual(avltree.get_time_complexity(), 'O(logn)')

    def test_remove_empty(self):
        """15. Test remove_empty tree."""
        self.assertEqual(self.avltree.remove(4), False)

    def test_remove_non_existent(self):
        """16. Test remove non-existent value."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.insert(10)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        self.assertEqual(avltree.find_helper(self.avltree.root, 1), True)
        self.assertEqual(self.avltree.remove(100), False)

    def test_check_balance(self):
        """17. Test check balance."""
        self.avltree.insert(1)
        self.avltree.insert(2)
        self.avltree.insert(3)
        self.avltree.insert(4)
        self.avltree.insert(5)
        self.avltree.remove(5)
        self.avltree.insert(10)
        self.avltree.remove(3)
        self.avltree.insert(9)
        self.avltree.insert(8)
        self.avltree.remove(10)
        self.avltree.remove(8)
        self.avltree.insert(7)
        self.avltree.insert(6)
        balance_height = avltree.balance(self.avltree.root)
        if balance_height <= 1:
            return True
        return False

    def test_remove_left_right_rotate(self):
        """18. Test right_leftremove."""
        self.avltree.insert(12)
        self.avltree.insert(1)
        self.avltree.insert(8)
        self.avltree.insert(2)
        self.avltree.remove(12)

    def test_balance_non_imput(self):
        """19. Test balance with none input."""
        self.assertEqual(avltree.balance(self.avltree.root), 0)
