class Solution:
    def getFrequency(self, s):
        dict_freq = {}
        for c in s:
            dict_freq[c] = dict_freq.get(c, 0) + 1
        return dict_freq

    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        if k == len(s):
            return True
        if k > 26 and len(s) > 26:
            return True
        dict_freq=self.getFrequency(s)
        oc = 0
        for freq in dict_freq.values():
            if freq % 2 == 1:
                oc += 1
        if oc <= k:
            return True
        else:
            return False
