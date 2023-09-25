class Deque:
    def __init__(self):
        self.deque = list()

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        self.deque.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        self.deque.pop()

    def size(self):
        return len(self.deque)

    def __eq__(self, other: list):
        return self.deque == other
