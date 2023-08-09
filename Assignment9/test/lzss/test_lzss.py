"""Test LZSS implementation."""


import unittest
import logging
import sys
# import random
# import string
from compression.lzss import lzss


class LZSSTest(unittest.TestCase):
    """Class LZSS."""

    def setUp(self):
        """Setup."""
        debug = True
        self.lzss = lzss.LZSS()
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("LZSSTestLog")

    def test_lzss_1(self):
        """1. Test LZSS_1 ."""
        indata = 'cars' * 100
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_2(self):
        """2. Test LZSS_2 ."""
        indata = 'I am Sam\n\n'
        indata += 'Sam I am\n\nThat Sam-I-am!\nThat Sam-I-am!\nI do not like\nthat Sam-I-am'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_3(self):
        """3. Test LZSS_3 ."""
        indata = 'aaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaa'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_4(self):
        """4. Test LZSS_4."""
        indata = 'aaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaa'*10
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_5(self):
        """5. Test LZSS_5."""
        indata = 'ABCDEFGHJKLABCDEF'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_6(self):
        """6. Test LZSS_6."""
        indata = 'I am Steven Finish Homework I am Steven'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_7(self):
        """7. Test LZSS_7."""
        indata = 'I am Steven Finish Homework I am Steven' * 10
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_8(self):
        """8. Test LZSS_8."""
        indata = 'Hiring me Firmware Engineering!!!\n Firmware' * 10
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_9(self):
        """9. Test LZSS_9."""
        indata = 'FIND A JOB/Intern!!!' * 100
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_10(self):
        """10. Test LZSS_10."""
        indata = 'ENCODING encoding DECODING decoding'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_11(self):
        """11. Test LZSS_11."""
        indata = 'LZSS_LZSS_LZSS\n\nLZSSLZSS_LZSS'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_12(self):
        """12. Test LZSS_12."""
        indata = 'ABCD ABCD DEFG PLKG' * 10
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_13(self):
        """13. Test LZSS_13."""
        indata = 'SCHool school School SCHool'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)

    def test_lzss_14(self):
        """14. Test LZSS_14."""
        indata = 'ECEN 1100 ECEN 8999 ECEN'
        encoding = self.lzss.lzss_encode(indata)
        decoding = self.lzss.lzss_decode(encoding)
        self.assertEqual(decoding, indata)
        print('\n')
        print(encoding)
