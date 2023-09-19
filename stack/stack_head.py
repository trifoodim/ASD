from linked_list.class_linked_list import Node, LinkedList


class StackFromHead:
    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return self.stack.len()

    def pop(self):
        if self.size() != 0:
            ans = self.stack.head.value
            self.stack.head = self.stack.head.next
            return ans
        else:
            return None

    def push(self, value):
        self.stack.insert(None, Node(value))

    def peek(self):
        if self.size != 0:
            return self.stack.head.value
        else:
            return None

    def __str__(self):
        node = self.stack.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        print(f'{nodes}')
