class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __str__(self):
        string = ''
        for i in range(self.size()):
            string += f'{self.queue[i]},'
        return string
