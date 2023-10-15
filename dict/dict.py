class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def find_slot(self, key):
        hash_idx = self.hash_fun(key)
        for i in range(self.size):
            if (self.slots[hash_idx] is None) or (self.slots[hash_idx] == key):
                return hash_idx
            hash_idx += 1
            if hash_idx >= self.size:
                hash_idx %= self.size
        return None

    def hash_fun(self, key):
        return sum(ord(symb) for symb in key) % self.size

    def is_key(self, key):
        keys_slot = self.find_slot(key)
        return keys_slot is not None and self.slots[keys_slot] is not None

    def put(self, key, value):
        keys_slot = self.find_slot(key)
        self.slots[keys_slot] = key
        self.values[keys_slot] = value

    def get(self, key):
        keys_slot = self.find_slot(key)
        return None if keys_slot is None else self.values[keys_slot]
