"""test fib implementation."""

import unittest
import logging
import sys
from unittest.result import failfast
from fibonacci.fib import fib


class FibTest(unittest.TestCase):
    """Class FibTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.fib = fib.Fib()

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("FibTestLog")

    def test_function0(self):
        """input0."""
        return self.assertEqual(self.fib.calculate(0), None)

    def test_function1(self):
        """input1."""
        return self.assertEqual(self.fib.get_fib(1), 1)

    def test_method1_noin(self):
        """Loop method with none input."""
        return self.assertEqual(self.fib.get_fib(None), None)

    def test_method1_small(self):
        """Loop method with small sequence."""
        self.assertEqual(self.fib.get_fib(13), 233)

    def test_method1_large(self):
        """loop method with large sequence."""
        self.assertEqual(self.fib.get_fib(1000), self.fib.get_fib(1000))

    def test_method2_noin(self):
        """Recursion method with none input."""
        self.assertEqual(fib.calculate_fib(None), None)

    def test_method2_0input(self):
        """Recursion method with 0 input"""
        self.assertEqual(fib.calculate_fib(0), 0)

    def test_method2_small(self):
        """Recursion method with small sequence"""
        self.assertEqual(fib.calculate_fib(3), 2)

    @failfast
    def test_method2_large(self):
        """Recursion method with large sequence"""
        self.assertEqual(fib.calculate_fib(10), self.fib.get_fib(10))
