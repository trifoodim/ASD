class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        res = 0
        base = 17
        for c in key:
            code = ord(c)
            res = (res * base + code) % self.size
        return res

    def __seek_slot(self, key):
        hash_idx = self.hash_fun(key)
        for i in range(self.size):
            if (self.slots[hash_idx] is None) or (self.slots[hash_idx] == key):
                return hash_idx
            hash_idx += 1
            if hash_idx >= self.size:
                hash_idx %= self.size
        return None

    def __seek_drop_slot(self, key):
        s = 0
        for i in range(1, self.size):
            if self.hits[i] < self.hits[s]:
                s = i
        return s

    def is_key(self, key):
        seek_slot = self.__seek_slot(key)
        return (seek_slot is not None) and (self.slots[seek_slot] is not None)

    def put(self, key, value):
        seek_slot = self.__seek_slot(key)
        if seek_slot is None:
            seek_slot = self.__seek_drop_slot(key)
            self.hits[seek_slot] = 0
        self.slots[seek_slot] = key
        self.values[seek_slot] = value

    def get(self, key):
        seek_slot = self.__seek_slot(key)
        if seek_slot is None:
            return None
        else:
            self.hits[seek_slot] += 1
            return self.values[seek_slot]