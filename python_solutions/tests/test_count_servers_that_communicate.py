import unittest
from ..count_servers_that_communicate import Solution

class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().countServers([[1,0],[0,1]]), 0)

    def test_second(self):
        self.assertEqual(Solution().countServers([[1,0],[1,1]]), 3)

    def test_third(self):
        self.assertEqual(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]), 4)


if __name__ == "__main__":
    unittest.main()
