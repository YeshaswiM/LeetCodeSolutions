from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        t = len(nums) - 1
        while b <= t:
            ptr = b + (t - b) // 2
            if nums[b] == target: 
                return b
            if nums[t] == target:
                return t
            if nums[ptr] == target:
                return ptr
            elif nums[ptr] > target:
                t = ptr - 1 
            elif nums[ptr] < target:
                b = ptr + 1 
        return -1
