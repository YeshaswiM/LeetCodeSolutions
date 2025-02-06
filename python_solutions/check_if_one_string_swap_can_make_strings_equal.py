class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Return True is entire strings are same
        if s1 == s2: 
            return True
        notequal_ct = 0
        mismatchidx = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if mismatchidx >= 0:
                    if s1[mismatchidx] == s2[i] and s1[i] == s2[mismatchidx]:
                        notequal_ct += 1 
                    else:
                        return False
                else:
                    mismatchidx = i
                    notequal_ct += 1 
            if notequal_ct > 2:
                break
        if notequal_ct == 2:
            return True        
        return False
