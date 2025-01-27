import unittest
from ..island_perimeter import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16)

    def test_second(self):
        self.assertEqual(Solution().islandPerimeter([[1]]), 4)

    def test_third(self):
        self.assertEqual(Solution().islandPerimeter([[1,0]]), 4)


if __name__ == "__main__":
    unittest.main()
