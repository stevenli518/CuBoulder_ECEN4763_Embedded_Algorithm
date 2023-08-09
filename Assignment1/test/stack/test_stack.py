"""test stack implementation."""


import unittest
import logging
import sys
from structures.stack import stack


class ArrayTest(unittest.TestCase):
    """Class StackTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.stack = stack.Stack(8)
        self.stack.stack = [1, 2, 3, 4, 5, 6, 7, 8]
        self.stack.maxsize = len(self.stack.stack)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("StackTestLog")

    def test_stack_isempty(self):
        """1.Check if the stack is empty."""
        self.stack.stack = []
        self.assertEqual(self.stack.isempty(), True)

    def test_stack_is_not_empty(self):
        """2.Check if the stack is not empty."""
        self.assertEqual(self.stack.isempty(), False)

    def test_stack_pop(self):
        """3.Pop element from a full stack and check the change of the size."""
        size_old = self.stack.stack_size()
        self.stack.pop()
        size_new = self.stack.stack_size()
        self.assertEqual(size_old-1, size_new)

    def test_stack_pop_empty(self):
        """4.Pop element from a empty stack and expect to see False."""
        self.stack.stack = []
        self.assertEqual(self.stack.pop(), False)

    def test_stack_push(self):
        """5.Push element to a empty stack and expect to see size +1."""
        self.stack.stack = []
        size_old = self.stack.stack_size()
        self.stack.push(1)
        size_new = self.stack.stack_size()
        self.assertEqual(size_old+1, size_new)

    def test_stack_push_full(self):
        """6.Push element to a full stack and expect to see False."""
        self.assertEqual(self.stack.push(1), False)

    def test_check_pop_order(self):
        """7.Pop element from a full stack and top_peak the value of the stack."""
        self.stack.pop()
        self.assertEqual(self.stack.top_peek(), 7)
        self.stack.pop()
        self.assertEqual(self.stack.top_peek(), 6)

    def test_check_push_order(self):
        """8.Push element into a empty stack and top_peak the value of the stack."""
        self.stack.empty()
        self.stack.push(1)
        self.assertEqual(self.stack.top_peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top_peek(), 2)

    def test_check_pop_n_push_order(self):
        """9.Push element into a empty stack, Pop element from the stack."""
        self.stack.empty()
        self.stack.push(1)
        self.assertEqual(self.stack.top_peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top_peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.top_peek(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.isempty(), True)

    def test_check_maxsize(self):
        """10.Check the maxsize."""
        self.assertEqual(self.stack.maxsize, self.stack.stack_size())

    def test_top_peak_full_stack(self):
        """11.Top peak the full stack."""
        self.assertEqual(self.stack.top_peek(), 8)

    def test_top_peak_empty_stack(self):
        """12.Top peak an empty stack."""
        self.stack.empty()
        self.assertEqual(self.stack.top_peek(), None)

    def test_empty_function(self):
        """13.Check the empty function."""
        self.stack.empty()
        self.assertEqual(self.stack.stack_size(), 0)

    def test_stack_size_function(self):
        """14.Check stack_size() function."""
        self.assertEqual(self.stack.stack_size(), len(self.stack.stack))

    def test_sapce_complexity_function(self):
        """15.Check space comlexity function."""
        self.assertEqual(stack.get_space_complexity(), 'O(n)')
