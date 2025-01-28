import unittest
from ..set_matrix_zeroes import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])

    def test_second(self):
        self.assertEqual(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

    def test_third(self):
        self.assertEqual(Solution().setZeroes([[0],[1]]), [[0],[0]])


if __name__ == "__main__":
    unittest.main()
