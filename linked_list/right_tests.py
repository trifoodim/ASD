import ctypes
import unittest

from class_linked_list import LinkedList, Node


class TestLinkedListMethods(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.node1 = Node(1)
        self.node2_1 = Node(2)
        self.node2_2 = Node(2)
        self.node3_1 = Node(3)
        self.node3_2 = Node(3)
        self.node3_3 = Node(3)
        self.node55_1 = Node(55)
        self.node55_2 = Node(55)

    def test_add_in_tail(self):  # passed
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

        self.linked_list.add_in_tail(self.node1)

        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node1)

        self.linked_list.add_in_tail(self.node2_1)

        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node2_1)

        self.linked_list.add_in_tail(self.node3_1)

        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node3_1)

        self.linked_list.add_in_tail(self.node2_2)

        self.assertEqual(self.linked_list.head, self.node1)
        self.assertNotEqual(self.linked_list.tail, self.node2_1)
        self.assertEqual(self.linked_list.tail, self.node2_2)

    def test_delete_only_one_node(self):
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.delete(1)

        self.assertIsNotNone(self.linked_list.head)
        self.assertIsNotNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.head, self.node2_1)
        self.assertEqual(self.linked_list.tail, self.node2_1)

        self.assertEqual(self.node2_1, self.linked_list.tail)

        self.linked_list.delete(2)

        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertNotEqual(self.linked_list.tail, self.node2_1)

    def test_delete_one_node(self):  # passed
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.add_in_tail(self.node3_1)
        self.linked_list.add_in_tail(self.node2_2)

        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertNotEqual(self.linked_list.tail, self.node2_1)
        self.assertEqual(self.linked_list.tail, self.node2_2)

        self.assertIsNotNone(self.node3_1.next)
        self.assertIsNone(self.node2_2.next)

        self.linked_list.delete(4)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node2_2)

        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node3_1)
        self.linked_list.delete(3)

        self.assertEqual(self.linked_list.len(), 1)
        self.assertEqual(self.linked_list.tail, self.node1)

    def test_delete_all_node(self):  # passed
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.add_in_tail(self.node3_1)
        self.linked_list.add_in_tail(self.node2_2)

        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node2_2)

        self.linked_list.delete(1)
        self.linked_list.delete(3)

        self.assertEqual(self.linked_list.head, self.node2_1)
        self.assertEqual(self.linked_list.tail, self.node2_2)

        self.linked_list.delete(2, True)

        self.linked_list.print_all_nodes()
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertIsNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node3_1)

        self.linked_list.delete(3)

        self.assertEqual(self.linked_list.len(), 1)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node1)

    def test_clean(self):  # passed
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.add_in_tail(self.node3_1)

        self.linked_list.clean()

        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_find(self):  # tests passed
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.add_in_tail(self.node3_1)

        self.assertEqual(self.linked_list.find(2), self.node2_1)
        self.assertIsNone(self.linked_list.find('a4'))

    def test_find_all(self):  # tests don't passed, loop of circle
        self.linked_list.add_in_tail(self.node1)
        self.linked_list.add_in_tail(self.node2_1)
        self.linked_list.add_in_tail(self.node3_1)
        self.linked_list.add_in_tail(self.node2_1)

        self.assertEqual(self.linked_list.find_all(2), [self.node2_1, self.node2_2])

        found_nodes = self.linked_list.find_all(2)
        self.assertEqual(len(found_nodes), 2)
        self.assertEqual(found_nodes[2], [self.node2_1, self.node2_2])
        self.assertEqual(found_nodes[1], self.node2_1)
        
        found_nodes = self.linked_list.find_all(4)
        self.assertEqual(len(found_nodes), 0)

    def test_len(self):  # tests passed
        self.linked_list.add_in_tail(self.node1)
        self.assertEqual(self.linked_list.len(), 1)

        self.linked_list.add_in_tail(self.node2_1)
        self.assertEqual(self.linked_list.len(), 2)

        self.linked_list.add_in_tail(self.node3_1)
        self.assertEqual(self.linked_list.len(), 3)

        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.len(), 2)

    def test_insert(self):  # test passed
        self.linked_list.insert(None, self.node1)
        self.assertEqual(self.linked_list.head, self.node1)
        self.assertEqual(self.linked_list.tail, self.node1)

        self.linked_list.insert(self.node1, self.node2_1)
        self.assertEqual(self.linked_list.head, self.node1)


if __name__ == '__main__':
    unittest.main()
