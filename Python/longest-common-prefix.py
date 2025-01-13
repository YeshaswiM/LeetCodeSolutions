 from typing import List
 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        if not len(strs[0]):
            return ""
        if len(strs)==1:
            return strs[0]
        # Check if entire first word matches entire string
        if len(set(strs))==1:
            return strs[0]
        pfend=-1
        retstrr=""
        for idx in range(len(strs[0])):
            if idx>=0:
                pfx=strs[0][0:idx+1]
                b = list(map(lambda x: True if x.startswith(pfx) else False, strs))
                if all(b):
                    pfend=idx
                    retstrr=pfx
                    continue
                else:
                    break
        if pfend>=0:
            return retstrr
        else:
            return ""
