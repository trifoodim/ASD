import unittest

from dict import NativeDictionary


class Test(unittest.TestCase):
    def test(self):
        d = NativeDictionary(6)
        kv = {
            "first_key": 1,
            "second_key": 2,
            "third_key": 3,
            "fourth_key": 4,
            "fifth_key": 5,
            "sixth_key": 6,
        }

        self.assertFalse(d.is_key("first_key"))
        self.assertIsNone(d.get("first_key"))

        for k, v in kv.items():
            d.put(k, v)

        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)

        kv["second_key"] = 100
        d.put("second_key", 100)
        kv["fifth_key"] = 254
        d.put("fifth_key", 254)

        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)

        self.assertFalse(d.is_key("foo"))
        self.assertIsNone(d.get("foo"))


if __name__ == "__main__":
    unittest.main()
