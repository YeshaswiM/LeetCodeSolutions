import unittest
from ..neighboring_bitwise_xor import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().doesValidArrayExist([1,1,0]))

    def test_second(self):
        self.assertEqual(Solution().doesValidArrayExist([1,1]))

    def test_third(self):
        self.assertEqual(Solution().doesValidArrayExist([1,0]))


if __name__ == "__main__":
    unittest.main()
