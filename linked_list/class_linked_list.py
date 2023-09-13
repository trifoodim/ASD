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
        node = self.head
        while node is not None:
            if node.value == val:
                ans.append(node)
            node = node.next

        return ans

    def delete(self, val, all=False):
        if self.head is None:
            return

        if self.head.value == val:
            if self.head == self.tail:
                self.tail = self.head.next

            self.head = self.head.next
            if not all:
                return

        current = self.head

        while current.next is not None:
            if current.next.value == val and current.next is self.tail:
                self.tail = current

            elif current.next.value == val:
                current.next = current.next.next
                if not all:
                    return
            else:
                current = current.next

    def clean(self):
        current = self.head
        while current:
            node_next = current.next
            del current
            current = node_next

        self.head = None
        self.tail = None

    def len(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode

        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
