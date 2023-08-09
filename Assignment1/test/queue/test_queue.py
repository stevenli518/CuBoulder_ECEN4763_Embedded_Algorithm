"""test queue implementation."""

import unittest
import logging
import sys
from structures.queue import queue


class ArrayTest(unittest.TestCase):
    """Class QueueTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.queue = queue.Queue(8)
        self.queue.queue = [1, 2, 3, 4, 5, 6, 7, 8]
        self.queue.maxsize = len(self.queue.queue)
        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("QueueTestLog")

    def test_isnot_empty(self):
        """1.Check if the queue is not empty."""
        return self.assertEqual(self.queue.isempty(), False)

    def test_is_empty(self):
        """2.Check if the queue is empty."""
        self.queue.empty()
        return self.assertEqual(self.queue.isempty(), True)

    def test_enqueue_empty(self):
        """3.Enqueue 10 when the queue is empty."""
        self.queue.empty()
        self.queue.enqueue(10)
        return self.assertEqual(self.queue.queue_size(), 1)

    def test_enqueue_full(self):
        """4.Enqueue 10 when the queue is full."""
        return self.assertEqual(self.queue.enqueue(10), False)

    def test_dequeue_empty(self):
        """5.Enqueue 10 when the queue is empty."""
        self.queue.empty()
        re_val = self.queue.dequeue()
        return self.assertEqual(re_val, False)

    def test_dequeue_full(self):
        """6.Enqueue 10 when the queue is full."""
        size = self.queue.queue_size()
        self.queue.dequeue()
        return self.assertEqual(self.queue.queue_size(), size-1)

    def test_check_order_dequeue(self):
        """7.Check the order_dequeue"""
        de_val = self.queue.dequeue()
        self.assertEqual(de_val, 1)

    def test_check_order_enqueue(self):
        """8.Check the order_dequeue"""
        self.queue.dequeue()
        en_val = self.queue.enqueue(9)
        self.assertEqual(en_val, 9)

    def test_check_order_enq_n_deq(self):
        """9.Check the order_dequeue"""
        de_val = self.queue.dequeue()
        self.assertEqual(de_val, 1)
        en_val = self.queue.enqueue(99)
        self.assertEqual(en_val, 99)

    def test_max_size(self):
        """10.Check the max size of Queue."""
        return self.assertEqual(self.queue.queue_size(), self.queue.maxsize)

    def test_space_complexity(self):
        """11.Space complxity."""
        self.assertEqual(queue.get_space_complexity(), 'O(n)')

    def test_queue_size(self):
        """12.Check queue size"""
        self.assertEqual(self.queue.queue_size(), 8)

    def test_empty_queue_size(self):
        """13.Check queue size"""
        self.queue.empty()
        self.assertEqual(self.queue.queue_size(), 0)

    def test_empty_function2(self):
        """14.Check empty function."""
        self.queue.empty()
        self.queue.enqueue(0)
        self.assertEqual(self.queue.isempty(), False)
