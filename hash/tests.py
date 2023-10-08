class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash_key = sum(ord(element) for element in value)
        return hash_key % self.size

    def seek_slot(self, value):
        hash_index = self.hash_fun(value)

        for i in range(self.size):
            if self.slots[hash_index] is None:
                return hash_index
            
            hash_index += self.step
            if hash_index >= self.size:
                hash_index %= self.size

        return None

    def put(self, value):
        hash_available = self.seek_slot(value)
        if self.slots[hash_available] is not None:
            self.slots[hash_available] = value
        return None

    def find(self, value):
        hash_index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[hash_index] == value:
                return hash_index
            hash_index += self.step
            if hash_index >= self.size:
                hash_index %= self.size

        return None
