import unittest
from ..check_if_one_string_swap_can_make_strings_equal import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().areAlmostEqual("bank", "kanb"), True)

    def test_second(self):
        self.assertEqual(Solution().areAlmostEqual("attack", "defend"), False)
        
    def test_third(self):
        self.assertEqual(Solution().areAlmostEqual("kelb", "kelb"), True)


if __name__ == "__main__":
    unittest.main()