"""Test HYBRID implementation."""


import unittest
import logging
import sys
import random
import string
from compression.hybrid import hybrid
# pylint: disable = R0904


class HybridTest(unittest.TestCase):
    """Class HYBRID."""

    def setUp(self):
        """Setup."""
        debug = True
        self.bwt = hybrid.BWT()
        self.rle = hybrid.RLE()
        self.hybrid = hybrid.Hybrid()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("hybridTestLog")

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

    def test_bwt_1(self):
        """1. Test bwt_1 ."""
        my_string = 'Test input. Test input. Test input.'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_2(self):
        """2. Test bwt_2."""
        my_string = 'Peter Piper'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_3(self):
        """3. Test bwt_3."""
        my_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_4(self):
        """4. Test bwt_4."""
        my_string = 'aaaaaaaaaaaaaa'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_5(self):
        """5. Test bwt5."""
        my_string = 'b' * 111
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_6(self):
        """6. Test bwt_6."""
        my_string = 'c' * 100
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_7(self):
        """7. Test bwt_7."""
        my_string = 'a' * 25 + 'b' * 10
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_8(self):
        """8. Test bwt_8."""
        my_string = 'a' * 55 + 'b' * 10 + 'g'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_9(self):
        """9. Test bwt_9."""
        my_string = ''
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_10(self):
        """10. Test bwt_10."""
        my_string = 'a' * 10 + 'g' * 15 + 'e' * 29 + 'f' * 12 + 'g'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_11(self):
        """11. Test bwt_11."""
        my_string = 'jkm' * 55
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_12(self):
        """12. Test bwt_12."""
        my_string = '*' * 12
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_13(self):
        """13. Test bwt_13."""
        my_string = 'abcddddeefff!)@@@'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_bwt_14(self):
        """14. Test bwt_14."""
        my_string = '!!!!!!!///////*********-------+-=odadadadOOOO'
        encoding = self.bwt.bw_transform(my_string)
        decoding = self.bwt.bw_inv_transform(encoding)
        self.assertEqual(my_string, decoding)

    def test_hybrid_1(self):
        """1. Test hybrid_1 ."""
        my_string = 'Test input. Test input. Test input.'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_2(self):
        """2. Test hybrid_2 ."""
        my_string = ''
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_3(self):
        """2. Test hybrid_3 ."""
        my_string = 'a' * 60
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_4(self):
        """2. Test hybrid_4 ."""
        my_string = 'abc' * 100
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_5(self):
        """5. Test hybrid_5."""
        my_string = '!!!@#$' * 12
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_6(self):
        """6. Test hybrid_6 ."""
        my_string = 'Steven Finds an Intern'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_7(self):
        """7. Test hybrid_7 ."""
        my_string = '\n\n\n' * 12
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_8(self):
        """8. Test hybrid_8 ."""
        my_string = 'Chengming Li\n\nMaster'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_9(self):
        """9. Test hybrid_9 ."""
        my_string = '..!..!..!.'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_10(self):
        """10. Test hybrid_10 ."""
        my_string = 'qwertyuiopasdfghjkl'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_11(self):
        """11. Test hybrid_11 ."""
        my_string = '////////!@#!@#!'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_12(self):
        """12. Test hybrid_12 ."""
        my_string = 'AAAAQEQWEQ' * 10
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_13(self):
        """13. Test hybrid_13 ."""
        my_string = '[][][][][]'
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)

    def test_hybrid_14(self):
        """14. Test hybrid_14 ."""
        my_string = ':) :(' * 10
        result = self.hybrid.hybrid_encode(my_string)
        decode = self.hybrid.hybrid_decode(result)
        self.assertEqual(my_string, decode)
