"""test array implementation."""

import unittest
import logging
import sys
from structures.array import array


class ArrayTest(unittest.TestCase):
    """Class ArrayTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.ary = array.Array()
        self.ary.array = [1, 2, 3, 4, 5, 6, 7, 8]
        array.Array.array = self.ary.array
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("ArrayTestLog")

    def test_insert_beg(self):
        """1.insert at begnning."""
        self.ary.insert(99, 0)
        return self.assertEqual(self.ary.array[0], 99)

    def test_insert_middle(self):
        """2.insert at the middle."""
        self.ary.insert(99, 3)
        return self.assertEqual(self.ary.array[3], 99)

    def test_inset_end(self):
        """3.insert at the end."""
        self.ary.insert(100, -1)
        return self.assertEqual(self.ary.array[len(self.ary.array)-1], 100)

    def test_insert_n_verify_size(self):
        """4.insert and verify the size changes."""
        size_old = array.get_size()
        self.ary.insert(1000, -1)
        size_new = array.get_size()
        self.assertEqual(size_new, size_old+1)

    def test_empty_remove(self):
        """5.verify empty removes all elements."""
        array.empty()
        self.assertEqual(array.is_empty(), True)

    def test_insert_verify(self):
        """6.insert an element and verify it exists."""
        self.ary.insert(678, -1)
        self.assertEqual(array.exists(678), True)

    def test_space_complexity(self):
        """7.Space complxity."""
        self.assertEqual(array.get_space_complexity(), 'O(n)')

    def test_corner_cases(self):
        """8.corner cases"""
        array.Array()
        self.assertEqual(array.remove(1), None)

    def test_get_values(self):
        """9.Get_values"""
        self.assertEqual(array.get_value(1), 2)

    def test_get_values_none(self):
        """10.Get_values_none"""
        self.assertEqual(array.get_value(99), None)

    def test_index_remove_none(self):
        """11.index none"""
        array.Array()
        self.assertEqual(array.remove(1), None)

    def test_remove(self):
        """12.Remove 3"""
        self.assertEqual(array.remove(3), 3)

    def test_is_empty(self):
        """13.is_empty"""
        array.empty()
        self.assertEqual(array.is_empty(), True)

    def test_is_not_empty(self):
        """14.is_not_empty"""
        self.assertEqual(array.is_empty(), False)

    def test_is_exist(self):
        """15.Is_exist"""
        self.assertEqual(array.exists(4), True)

    def test_is_not_exist(self):
        """16.Is_not_exist"""
        self.assertEqual(array.exists(100), False)

    def test_index_specific(self):
        """17.Get index specific"""
        self.assertEqual(array.get_index(99), None)

    def test_print(self):
        """18.Test print function"""
        self.ary.print_array()
        return True
