from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Method 1 - To get a valid original array, 
        # by commutative and self inverse property of XOR,
        # XOR of all elements (allxor) of derived must be 0
        # allxor = 0
        # for d in derived:
        #     allxor ^= d
        # return allxor == 0
        # Method 2 - much faster than calculating XOR
        # If derived contains odd number of 1, allxor will be 1
        return derived.count(1) % 2 == 0
