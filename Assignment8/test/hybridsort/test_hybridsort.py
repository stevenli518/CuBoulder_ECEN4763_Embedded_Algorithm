"""Test hybrid sort implementation."""


import unittest
import logging
import sys
import random
import string
from sort.hybridsort import hybridsort


class HybridsortTest(unittest.TestCase):
    """Class Insertionsort."""

    def setUp(self):
        """Setup."""
        debug = True
        self.array = hybridsort.HybridSort()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("hybridTestLog")

    def test_init(self):
        """1. Test mergesort constructor."""
        print(self.array.array)

    def test_get_time_complexity(self):
        """2. Test time complexity."""
        self.assertEqual(hybridsort.get_time_complexity(), 'O(nlogn)')

    def test_get_space_complexity(self):
        """3. Test space complexity."""
        self.assertEqual(hybridsort.get_space_complexity(), 'O(n)')

    def test_mergesort(self):
        """4. Test timsort."""
        test_arr = [random.uniform(-10000, 10000) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.array, test_arr)

    def test_mergesort2(self):
        """5. Test timsort2."""
        test_arr = [random.randint(-10000, 10000) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.array, test_arr)

    def test_mergesort3(self):
        """6. Test timsort3."""
        test_arr = [random.choice(string.ascii_letters) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.array, test_arr)

    def test_mergesort4(self):
        """7. Test timsort4."""
        letters = string.ascii_lowercase
        test_arr = [''.join(random.choice(letters) for i in range(5)) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.array, test_arr)

    def test_mergesort5(self):
        """8. Test timsort5."""
        test_arr = [random.choice(string.punctuation) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.array, test_arr)

    def test_mergesort6(self):
        """9. Test timsort6."""
        test_arr = [random.choice(string.punctuation) for _ in range(0, 1024)]
        test_arr = [1] + test_arr
        self.assertEqual(self.array.sort(test_arr), False)

    def test_mergesort7(self):
        """10. Test timsort7."""
        test_arr = [random.choice(string.punctuation) for _ in range(0, 1024)]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.get_sorted_list(), test_arr)

    def test_mergesort8(self):
        """11. Test timsort8."""
        test_arr = [1, 1, 3, 4, 5, 6, 8, 4]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.get_sorted_list(), test_arr)

    def test_mergesort9(self):
        """12. Test timsort9."""
        test_arr = ["a", "v", "z", "v", "c", "b", "d", "a"]
        self.array.sort(test_arr)
        test_arr.sort()
        self.assertEqual(self.array.get_sorted_list(), test_arr)

    def test_mergesort10(self):
        """13. Test timsort10."""
        test_arr = [1, "v", "z", "v", "c", "b", "d", "a"]
        self.assertEqual(self.array.sort(test_arr), False)

    def test_mergesort11(self):
        """14. Test timsort11."""
        test_arr = [10, 1, 3, 4, 5, 7, 8, 9]
        self.assertEqual(self.array.sort(test_arr), True)
