from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        highest = numsum = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i + 1] > nums[i]:
                numsum += nums[i]
            else:
                # If out of ascending order, reset
                highest = max(highest, numsum + nums[i])
                numsum = 0
        highest = max(highest, numsum)
        return highest
