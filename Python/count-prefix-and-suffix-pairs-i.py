from typing import List

class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        if str2.startswith(str1) and str2.endswith(str1): 
            return True
        else: 
            return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for idx,string in enumerate(words):
            # For each string, check if it is a prefix and suffix of subsequent strings
            for restofstring in words[idx+1::]:
                if len(string)<=len(restofstring):
                    if self.isPrefixAndSuffix(string,restofstring):
                        count+=1
        return count
