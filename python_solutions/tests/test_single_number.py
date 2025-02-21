import unittest
from ..single_number import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().singleNumber([2,2,1]), 1)

    def test_second(self):
        self.assertEqual(Solution().singleNumber([4,1,2,1,2]), 4)

    def test_third(self):
        self.assertEqual(Solution().singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()
