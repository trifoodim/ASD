class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        ans = []
        curr = self.head
        while curr is not None:
            if curr.value == val:
                ans.append(curr)
            curr = curr.next

        return ans

    def delete(self, val, all=False):
        if self.head is None:
            return

        if self.head.value == val:
            self.head = self.head.next
            if not all:
                return

        current = self.head
        prev = None

        while current is not None:
            if current.value == val:
                break
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

        if all:
            self.delete(val, all)

    def clean(self):
        curr = self.head
        while curr:
            node_next = curr.next
            del curr
            curr = node_next

        self.head = None

    def len(self):
        counter = 0
        curr = self.head
        while curr is not None:
            counter += 1
            curr = curr.next

        return counter

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode

        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
