import unittest
from ..minimum_recolors_to_get_k_consecutive_black_blocks import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().minimumRecolors("WBBWWBBWBW", 7), 3)

    def test_second(self):
        self.assertEqual(Solution().minimumRecolors("WBWBBBW", 2), 0)


if __name__ == "__main__":
    unittest.main()
