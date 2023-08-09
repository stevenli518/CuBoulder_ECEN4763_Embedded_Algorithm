"""Test RLE implementation."""


import unittest
import logging
import sys
import random
import string
from compression.rle import rle


class RLETest(unittest.TestCase):
    """Class RLE."""

    def setUp(self):
        """Setup."""
        debug = True
        self.rle = rle.RLE()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("RLETestLog")

    def test_rle_1(self):
        """1. Test RLE_1 ."""
        my_string = 'bbbccdefgggggggg'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_2(self):
        """2. Test RLE_2."""
        my_string = 'abcdefgh'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_3(self):
        """3. Test RLE_3."""
        my_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_4(self):
        """4. Test RLE_4."""
        my_string = 'aaaaaaaaaaaaaa'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_5(self):
        """5. Test RLE_5."""
        my_string = 'b' * 1000
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_6(self):
        """6. Test RLE_6."""
        my_string = 'c' * 1000
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_7(self):
        """7. Test RLE_7."""
        my_string = 'a' * 255 + 'b' * 100
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_8(self):
        """8. Test RLE_8."""
        my_string = 'a' * 255 + 'b' * 100 + 'g'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_9(self):
        """9. Test RLE_9."""
        my_string = 'a' * 1000 + 'g' + 'e' * 295 + 'f' * 122
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_10(self):
        """10. Test RLE_10."""
        my_string = 'a' * 10 + 'g' * 150 + 'e' * 295 + 'f' * 122 + 'g'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_11(self):
        """11. Test RLE_11."""
        my_string = 'jkm' * 1000
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_12(self):
        """12. Test RLE_12."""
        my_string = '*' * 1000
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_13(self):
        """13. Test RLE_13."""
        my_string = 'abcddddeefff!)@@@'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)

    def test_rle_14(self):
        """14. Test RLE_14."""
        my_string = '!!!!!!!///////*********-------+-=odadadadOOOO'
        result = self.rle.rle_encode(my_string)
        decode = self.rle.rle_decode(result)
        self.assertEqual(my_string, decode)
