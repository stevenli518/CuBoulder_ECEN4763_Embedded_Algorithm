"""Test hashmap implementation."""

# pylint: disable = R0904
import unittest
import logging
import sys
from structures.hashmap import hashmap


class HashmapTest(unittest.TestCase):
    """Class Hashmap."""

    def setUp(self):
        """Setup."""
        debug = True
        self.hashmap = hashmap.Hashmap(4)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("HashmapTestLog")

    def test_init(self):
        """1. Test the initialization."""
        print("\n")
        print(self.hashmap.hashmap)

    def test_add_value(self):
        """2. Test add_value function."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        print("\n")
        print(self.hashmap.hashmap)

    def test_add_value_update_value(self):
        """3. Test add_value function."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        print("\n")
        print(self.hashmap.hashmap)
        self.hashmap.add_value("A", 1111)
        print("\n")
        print(self.hashmap.hashmap)

    def test_add_value_same_bucket(self):
        """4. Test Add value to the same bucket."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        print("\n")
        print(self.hashmap.hashmap)
        self.hashmap.add_value("E", 1111)
        print("\n")
        print(self.hashmap.hashmap)

    def test_delete_value(self):
        """5. Test delete value."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        print("\n")
        print(self.hashmap.hashmap)
        self.hashmap.delete_value("A")
        print("\n")
        print(self.hashmap.hashmap)

    def test_delete_value_nonexistent(self):
        """6. Test delete value."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        print("\n")
        print(self.hashmap.hashmap)
        self.assertEqual(self.hashmap.delete_value("E"), None)

    def test_get_keys(self):
        """7. Test get_keys."""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("E", 1111)
        lst = self.hashmap.get_keys()
        print("\n")
        print(lst)

    def test_get_as_str(self):
        """8.Test get_as_str"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("E", 1111)
        lst = self.hashmap.get_as_str()
        print("\n")
        print(lst)

    def test_get_as_dict(self):
        """9.Test get_as_dict"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("E", 1111)
        my_dict = {}
        my_dict = self.hashmap.get_as_dict()
        print("\n")
        print(my_dict)

    def test_get_value(self):
        """10.Test get_value function"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("E", 1111)
        self.assertEqual(self.hashmap.get_value("A"), 111)

    def test_get_value_2(self):
        """11.Test get_value function_multivals"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("A", 1111)
        self.assertEqual(self.hashmap.get_value("A"), 1111)

    def test_check_forall_values_present(self):
        """12.Test all values are present"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("A", 1111)
        self.assertEqual(self.hashmap.get_value("A"), 1111)
        self.assertEqual(self.hashmap.get_value("B"), 222)
        self.assertEqual(self.hashmap.get_value("C"), 333)
        self.assertEqual(self.hashmap.get_value("D"), 444)

    def test_get_space_complexity(self):
        """13. Test get_space_complexity function"""
        self.assertEqual(hashmap.get_space_complexity(), 'O(n)')

    def test_get_time_complexity(self):
        """14. Test get_space_complexity function"""
        self.assertEqual(hashmap.get_time_complexity(), 'O(n) as worst case, O(1) as best case')

    def test_get_value_3(self):
        """15.Test get_value function: nonexistent key"""
        self.hashmap.add_value("A", 111)
        self.hashmap.add_value("B", 222)
        self.hashmap.add_value("C", 333)
        self.hashmap.add_value("D", 444)
        self.hashmap.add_value("E", 1111)
        self.assertEqual(self.hashmap.get_value("F"), None)
