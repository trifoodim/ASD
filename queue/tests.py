import unittest
from queue import rotation_of_queue


class MyTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.queue = self.queue()
        self.queue.enqueue(0)

    def test_enqueue(self):
        self.assertEqual(self.queue.__str__(), '0,')
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.__str__(), '0,1,2,3,')

    def test_dequeue(self):
        el = self.queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(self.queue.__str__(), '')

        el = self.queue.dequeue()
        self.assertEqual(el, None)
        self.assertEqual(self.queue.__str__(), '')

        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        el = self.queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(self.queue.__str__(), '1,2,3,')

    def test_rotate_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        rotation_of_queue(self.queue, 2)
        self.assertEqual(self.queue.__str__(), '3,4,0,1,2,')

        self.queue = self.queue()
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        rotation_of_queue(self.queue, 0)
        self.assertEqual(self.queue.__str__(), '0,1,2,3,4,')


if __name__ == '__main__':
    unittest.main()
