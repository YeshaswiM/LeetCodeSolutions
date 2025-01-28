from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        truster = [0] * (n + 1)
        trustee = [0] * (n + 1)
        # Get counts of truster and trustees for all n people
        for a,b in trust:
            truster[a] += 1
            trustee[b] += 1
        for i in range(n + 1):
            # Judge is the person that doesn't trust anyone and everyone else trusts them
            if truster[i] == 0 and trustee[i] == (n - 1):
                return i
        return -1
