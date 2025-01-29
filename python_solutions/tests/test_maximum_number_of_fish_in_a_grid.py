import unittest
from ..maximum_number_of_fish_in_a_grid import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]), 7)

    def test_second(self):
        self.assertEqual(Solution().findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]), 1)

if __name__ == "__main__":
    unittest.main()
