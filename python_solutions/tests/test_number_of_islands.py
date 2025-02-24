import unittest
from ..number_of_islands import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), 1)

    def test_second(self):
        self.assertEqual(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]), 3)

if __name__ == "__main__":
    unittest.main()
