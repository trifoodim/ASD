from stack.stack import Stack


class QueueWithStacks:
    def __init__(self):
        self.stack_for_enqueue = Stack()
        self.stack_for_dequeue = Stack()

    def enqueue(self, item):
        self.stack_for_enqueue.push(item)

    def dequeue(self):
        if self.stack_for_dequeue.size() == 0 and self.stack_for_enqueue.size() == 0:
            return None
        if self.stack_for_dequeue.size() == 0:
            while self.stack_for_enqueue.size() > 0:
                self.stack_for_dequeue.push(self.stack_for_enqueue.pop())
        return self.stack_for_dequeue.pop()

    def size(self):
        return self.stack_for_dequeue.size() or self.stack_for_enqueue.size()

    def __str__(self):
        string = ''
        string += 'enqueue: ' + self.stack_for_enqueue.__str__()
        string += 'dequeue: ' + self.stack_for_dequeue.__str__()
        return string
