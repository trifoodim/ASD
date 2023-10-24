class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0

    def hash1(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 17 + code) % self.filter_len
        return pow(2, res)

    def hash2(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 223 + code) % self.filter_len
        return pow(2, res)

    def add(self, str1):
        hs1 = self.hash1(str1)
        hs2 = self.hash2(str1)
        self.bit_array = self.bit_array | hs1
        self.bit_array = self.bit_array | hs2

    def is_value(self, str1):
        hs1 = self.hash1(str1)
        hs2 = self.hash2(str1)
        check_first = self.bit_array & hs1 != 0
        check_second = self.bit_array & hs2 != 0
        return check_first and check_second
