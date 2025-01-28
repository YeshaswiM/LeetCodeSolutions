import unittest
from ..find_the_town_judge import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().findJudge(2, [[1,2]]), 2)

    def test_second(self):
        self.assertEqual(Solution().findJudge(3, [[1,3],[2,3]]), 3)

    def test_third(self):
        self.assertEqual(Solution().findJudge(3, [[1,3],[2,3],[3,1]]), -1)

if __name__ == "__main__":
    unittest.main()
