import unittest

from stack_head import StackFromHead


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = StackFromHead()
        
    def test_size(self):
        
        self.assertEqual(self.stack.size(), 0)

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 3)

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.__str__()
        self.assertEqual(self.stack.__str__(), [2, 1, 0])

    def test_pop(self):
        el = self.stack.pop()
        self.assertEqual(el, None)
        self.assertEqual(self.stack.__str__(), [])

        self.stack.push(0)
        el2 = self.stack.pop()
        self.assertEqual(el2, 0)
        self.assertEqual(self.stack.__str__(), [])

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        el2 = self.stack.pop()
        self.assertEqual(el2, 3)
        self.assertEqual(self.stack.__str__(), [2, 1, 0])

    def test_peek(self):
        el = self.stack.peek()
        self.assertEqual(el, None)
        self.assertEqual(self.stack.__str__(), [])

        self.stack.push(0)
        el = self.stack.peek()
        self.assertEqual(el, 0)
        self.assertEqual(self.stack.__str__(), [0])


if __name__ == '__main__':
    unittest.main()
