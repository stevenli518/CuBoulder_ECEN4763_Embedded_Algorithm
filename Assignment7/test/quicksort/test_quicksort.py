"""Test insertion sort implementation."""


import unittest
import logging
import sys
from sort.quicksort import quicksort


class InsertionsortTest(unittest.TestCase):
    """Class Insertionsort."""

    def setUp(self):
        """Setup."""
        debug = True
        self.array = quicksort.QuickSort()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("BellmanfordTestLog")

    def test_init(self):
        """1. Test insertionsort constructor."""
        print(self.array.array)

    def test_get_time_complexity(self):
        """2. Test time complexity."""
        self.assertEqual(quicksort.get_time_complexity(), 'O(nlog(n))')

    def test_get_space_complexity(self):
        """3. Test space complexity."""
        self.assertEqual(quicksort.get_space_complexity(), 'O(N)')

    def test_insertionsort(self):
        """4. Test insertionsort."""
        self.assertEqual(self.array.sort(self.array.array), True)

    def test_insertionsort2(self):
        """5. Test insertionsort2."""
        array = [6, 6, 1, 1, 7, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort3(self):
        """6. Test insertionsort3."""
        array = [6, 1, 1, 6, 7, 8]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort4(self):
        """7. Test insertionsort4."""
        array = [6, 1, 1, 6, 6, 6]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort5(self):
        """8. Test insertionsort5."""
        array = [6, 1, 3, 'A', 9, 6]
        self.assertEqual(self.array.sort(array), False)
        print(self.array.array)

    def test_insertionsort6(self):
        """9. Test insertionsort6."""
        array = ['B', 'C', 'C', 'B', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort7(self):
        """10. Test insertionsort7."""
        array = ['B', 'B', 'Z', 'A', 'D', 'E']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort8(self):
        """11. Test insertionsort8."""
        array = [6.5, 1.66, 1.7, 6.8, 9.7, 6.4]
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort9(self):
        """12. Test insertionsort9."""
        array = ['b', 'cd', 'z', 'a', 'd', 'f']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort10(self):
        """13. Test insertionsort10."""
        array = ['bd', 'caa', 'zt', 'ab', 'de', 'fg']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)

    def test_insertionsort11(self):
        """14. Test insertionsort11."""
        array = ['%', '!!', '#', '*', '?', '!']
        self.assertEqual(self.array.sort(array), True)
        print(self.array.array)
