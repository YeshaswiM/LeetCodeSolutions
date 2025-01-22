import unittest
from ..binary_search import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().search([-1,0,3,5,9,12], 9), 4)

    def test_second(self):
        self.assertEqual(Solution().search([-1,0,3,5,9,12], 2), -1)


if __name__ == "__main__":
    unittest.main()