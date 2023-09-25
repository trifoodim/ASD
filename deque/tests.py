import unittest
from deque import Deque


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.deque = Deque()
        self.deque.addTail(1)
        self.deque.addTail(2)
        self.deque.addTail(3)
        self.deque.addTail(4)
        self.deque.addTail(5)

    def test_add_front(self):
        self.deque.addFront(0)
        self.assertIsNotNone(self.deque)
        self.assertEqual(self.deque, [0, 1, 2, 3, 4, 5])

    def test_add_tail(self):
        self.deque.addTail(6)
        self.assertIsNotNone(self.deque)
        self.assertEqual(self.deque, [1, 2, 3, 4, 5, 6])

    def test_remove_front(self):
        self.assertIsNotNone(self.deque)
        self.assertEqual(self.deque, [1, 2, 3, 4, 5])
        self.deque.removeFront()
        self.deque.removeFront()
        self.deque.removeFront()
        self.assertEqual(self.deque, [4, 5])
        self.deque.removeFront()
        self.deque.removeFront()
        self.assertEqual(self.deque, [])

    def test_remove_tail(self):
        self.assertIsNotNone(self.deque)
        self.assertEqual(self.deque, [1, 2, 3, 4, 5])
        self.deque.removeTail()
        self.deque.removeTail()
        self.assertEqual(self.deque, [1, 2, 3])
