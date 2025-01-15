import unittest
import sys
sys.path.append("..") 
from python_solutions.minimize_xor import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().minimizeXor(3, 2), 3)

    def test_second(self):
        self.assertEqual(Solution().minimizeXor(1, 12), 3)


if __name__ == "__main__":
    unittest.main()