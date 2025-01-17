from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        output = 0
        if len(nums1) & 1:
            if len(nums2) & 1:
                for l in nums1 + nums2:
                    output ^= l
            else:
                for l in nums2:
                    output ^= l
        else:
            if len(nums2) & 1:
                for l in nums1:
                    output ^= l
            else:
                output = 0
