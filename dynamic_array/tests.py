import unittest
from dynamic_array import DynArray


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dynamic_arr = DynArray()
        self.dynamic_arr.append(0)
        self.dynamic_arr.append(1)
        self.dynamic_arr.append(2)
        self.dynamic_arr.append(3)
        self.dynamic_arr.append(4)
        self.dynamic_arr.append(5)

    def test_insertion_out_of_range_index(self):  # passed
        with self.assertRaises(IndexError):
            self.dynamic_arr.insert(-1, 20)

        with self.assertRaises(IndexError):
            self.dynamic_arr.insert(100, 20)

    def test_insert(self):
        self.dynamic_arr.insert(3, 30)
        self.assertEqual(self.dynamic_arr.capacity, 16)
        self.assertEqual(self.dynamic_arr.count, 7)

        self.dynamic_arr._extend(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.dynamic_arr.insert(16, 150)
        self.assertEqual(self.dynamic_arr.capacity, 32)
        self.assertNotEqual(self.dynamic_arr.count, 17)

    def test_delete(self):
        self.assertEqual(self.dynamic_arr.capacity, 16)
        self.assertEqual(self.dynamic_arr.count, 6)

        dynamic_arr = DynArray()
        dynamic_arr._extend(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        dynamic_arr.delete(16)
        self.assertEqual(dynamic_arr.capacity, 32)
        self.assertEqual(dynamic_arr.count, 16)
        array = DynArray()._extend(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertNotEqual(dynamic_arr, array)

        dynamic_arr.delete(1)
        self.assertEqual(dynamic_arr.count, 15)
        self.assertEqual(dynamic_arr.capacity, 21)
        array = DynArray()._extend(0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertNotEqual(dynamic_arr, array)

        dynamic_arr.delete(0)
        dynamic_arr.delete(0)
        dynamic_arr.delete(0)
        dynamic_arr.delete(0)
        dynamic_arr.delete(0)
        self.assertEqual(dynamic_arr.count, 10)
        self.assertEqual(dynamic_arr.capacity, 16)
        array = DynArray()._extend(6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertNotEqual(dynamic_arr, array)

        with self.assertRaises(IndexError) as context:
            dynamic_arr.delete(20)

        dynamic_arr = DynArray()
        with self.assertRaises(IndexError) as context:
            dynamic_arr.delete(200)

        dynamic_arr = DynArray()
        dynamic_arr._extend(0, 1)
        dynamic_arr.delete(1)
        self.assertEqual(dynamic_arr.count, 1)
        self.assertEqual(dynamic_arr.capacity, 16)
        self.assertNotEqual(dynamic_arr, DynArray()._extend(0))


if __name__ == '__main__':
    unittest.main()