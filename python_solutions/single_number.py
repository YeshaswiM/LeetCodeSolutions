from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for el in nums:
            xor ^= el
        return xor
