class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(ord(c) for c in value) % self.size

    def seek_slot(self, value):
        hash_idx = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[hash_idx] is None:
                return hash_idx
            hash_idx += self.step
            if hash_idx >= self.size:
                hash_idx %= self.size
        return None

    def put(self, value):
        hash_idx = self.seek_slot(value)
        if hash_idx is not None:
            self.slots[hash_idx] = value
        return hash_idx

    def find(self, value):
        hash_idx = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[hash_idx] == value:
                return hash_idx
            hash_idx += self.step
            if hash_idx >= self.size:
                hash_idx %= self.size
        return None
