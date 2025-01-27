import unittest
from ..bitwise_xor_of_all_pairings import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().xorAllNums([2,1,3], [10,2,5,0]), 13)

    def test_second(self):
        self.assertEqual(Solution().xorAllNums([1,2], [3,4]), 0)


if __name__ == "__main__":
    unittest.main()