import unittest
from .minimize_xor_dupe import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().minimizeXor(3, 5), 3)

    def test_second(self):
        self.assertEqual(Solution().minimizeXor(1, 12), 3)


if __name__ == "__main__":
    unittest.main()