"""Test insertion sort implementation."""


import unittest
import logging
import sys
from sort.insertionsort import insertionsort


class InsertionsortTest(unittest.TestCase):
    """Class Insertionsort."""

    def setUp(self):
        """Setup."""
        debug = True
        self.array = insertionsort.InsertionSort()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("insertionsortTestLog")

    def test_init(self):
        """1. Test quicksort constructor."""
        print(self.array.array)

    def test_get_time_complexity(self):
        """2. Test time complexity."""
        self.assertEqual(insertionsort.get_time_complexity(), 'O(N^2)')

    def test_get_space_complexity(self):
        """3. Test space complexity."""
        self.assertEqual(insertionsort.get_space_complexity(), 'O(N)')

    def test_quicksort(self):
        """4. Test quicksort."""
        self.assertEqual(self.array.sort(self.array.array), True)

    def test_quicksort2(self):
        """5. Test quicksort2."""
        array = [6, 6, 1, 1, 9, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort3(self):
        """6. Test quicksort3."""
        array = [6, 1, 1, 6, 9, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort4(self):
        """7. Test quicksort4."""
        array = [6, 1, 1, 6, 9, 6]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort5(self):
        """8. Test quicksort5."""
        array = [6, 1, 1, 'A', 9, 6]
        self.assertEqual(self.array.sort(array), False)
        print(self.array.array)

    def test_quicksort6(self):
        """9. Test quicksort6."""
        array = ['B', 'C', 'D', 'A', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort7(self):
        """10. Test quicksort7."""
        array = ['B', 'C', 'Z', 'A', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort8(self):
        """11. Test quicksort8."""
        array = [6.5, 1.6, 1.7, 6.8, 9.7, 6.4]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort9(self):
        """12. Test quicksort9."""
        array = ['b', 'c', 'z', 'a', 'd', 'f']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort10(self):
        """13. Test quicksort10."""
        array = ['bd', 'ca', 'zt', 'ab', 'de', 'fg']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_quicksort11(self):
        """14. Test quicksort11."""
        array = ['%', '!', '#', '*', '?', '!']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)
