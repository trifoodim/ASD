class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.array_of_bites = 0

    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 17 + code) % self.filter_len
        return pow(2, result)

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % self.filter_len
        return pow(2, result)

    def add(self, str1):
        hs1 = self.hash1(str1)
        hs2 = self.hash2(str1)
        self.array_of_bites = self.array_of_bites | hs1
        self.array_of_bites = self.array_of_bites | hs2

    def is_value(self, str1):
        hs1 = self.hash1(str1)
        hs2 = self.hash2(str1)
        check_first_elem = self.array_of_bites & hs1 != 0
        check_second_elem = self.array_of_bites & hs2 != 0
        return check_first_elem and check_second_elem
