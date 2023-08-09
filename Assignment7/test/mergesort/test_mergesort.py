"""Test merge sort implementation."""


import unittest
import logging
import sys
from sort.mergesort import mergesort


class InsertionsortTest(unittest.TestCase):
    """Class Insertionsort."""

    def setUp(self):
        """Setup."""
        debug = True
        self.array = mergesort.MergeSort()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("mergesortTestLog")

    def test_init(self):
        """1. Test mergesort constructor."""
        print(self.array.array)

    def test_get_time_complexity(self):
        """2. Test time complexity."""
        self.assertEqual(mergesort.get_time_complexity(), 'O(nlog(n))')

    def test_get_space_complexity(self):
        """3. Test space complexity."""
        self.assertEqual(mergesort.get_space_complexity(), 'O(N)')

    def test_mergesort(self):
        """4. Test mergesort."""
        self.assertEqual(self.array.sort(self.array.array), True)

    def test_mergesort2(self):
        """5. Test mergesort2."""
        array = [6, 4, 1, 1, 9, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort3(self):
        """6. Test mergesort3."""
        array = [6, 1, 1, 6, 6, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort4(self):
        """7. Test mergesort4."""
        array = [6, 1, 1, 6, 1, 6]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort5(self):
        """8. Test mergesort5."""
        array = [6, 1, 2, 'A', 9, 6]
        self.assertEqual(self.array.sort(array), False)
        print(self.array.array)

    def test_mergesort6(self):
        """9. Test mergesort6."""
        array = ['C', 'C', 'D', 'A', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort7(self):
        """10. Test mergesort7."""
        array = ['B', 'C', 'A', 'A', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort8(self):
        """11. Test mergesort8."""
        array = [6.4, 1.6, 1.7, 6.8, 9.7, 6.4]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort9(self):
        """12. Test mergesort9."""
        array = ['bc', 'c', 'z', 'a', 'd', 'f']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort10(self):
        """13. Test mergesort10."""
        array = ['bc', 'ca', 'zt', 'ab', 'de', 'fg']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_mergesort11(self):
        """14. Test mergesort11."""
        array = ['%!', '!', '#', '*', '?', '!']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)
