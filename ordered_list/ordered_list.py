class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0

    def asc_to_num(self):
        return 1 if self.__ascending else -1

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.head.next = None
            return

        if self.compare(self.head.value, value) == self.asc_to_num():
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
            return

        elif self.compare(self.tail.value, value) != self.asc_to_num():
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        node = self.head
        while node.next is not None:
            if self.is_between_nodes(node, value):
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node
                return
            node = node.next

    def is_between_nodes(self, node, value):
        return self.compare(node.value, value) != self.asc_to_num() \
               and self.compare(node.next.value, value) in (self.asc_to_num(), 0)

    def find(self, val):
        if self.is_value_outside_range(val):
            return None

        node = self.head
        while node.next is not None:
            if node.value == val:
                return node
            if self.is_between_nodes(node, val) and self.compare(node.next.value, val) != 0:
                return None
            node = node.next

    def is_value_outside_range(self, val):
        return self.head is None \
               or self.compare(self.head.value, val) == self.asc_to_num() \
               or self.compare(self.tail.value, val) not in (0, self.asc_to_num())

    def delete(self, val):
        if self.is_value_outside_range(val):
            return
        if self.head.value == val and self.head.next is None:
            self.head = None
            self.tail = None
            return
        if self.head.value == val:
            self.head.next.prev = None
            self.head = self.head.next
            return
        if self.tail.value == val:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return
        node = self.head
        while node.next is not None:
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def __str__(self):
        node = self.head
        string = ''
        while node is not None:
            string += f'{node.value},'
            node = node.next
        return string


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1_stripped = v1.strip()
        v2_stripped = v2.strip()
        if v1_stripped > v2_stripped:
            return 1
        elif v1_stripped < v2_stripped:
            return -1
        else:
            return 0
