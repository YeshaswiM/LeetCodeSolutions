import unittest
from ..maximum_ascending_subarray_sum import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().maxAscendingSum([10,20,30,5,10,50]), 65)

    def test_second(self):
        self.assertEqual(Solution().maxAscendingSum([10,20,30,40,50]), 150)

    def test_third(self):
        self.assertEqual(Solution().maxAscendingSum([12,17,15,13,10,11,12]), 33)


if __name__ == "__main__":
    unittest.main()
