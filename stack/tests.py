import unittest
from stack import Stack


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)

    def test_size(self):
        self.assertEqual(self.stack.size(), 6)

    def test_push(self):
        self.stack.push(6)
        self.assertEqual(self.stack.size(), 7)
        self.stack.__str__()

        self.stack.push(7)
        self.stack.push(8)
        self.assertNotEqual(self.stack.size(), 8)
        self.stack.__str__()

    def test_peak(self):
        self.stack.__str__()
        self.assertEqual(self.stack.peek(), 5)
        self.stack.__str__()

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 5)
        self.stack.__str__()
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)
        self.assertNotEqual(self.stack.pop(), 3)
        self.stack.__str__()

