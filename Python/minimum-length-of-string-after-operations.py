class Solution:
    def minimumLength(self, s: str) -> int:
        # if string has less than 3 chars, no operation can be done
        if(len(s) < 3):
            return len(s)
        min_len = 0
        # Initialize a fixed map of chars to get char count
        set_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for c in set_s:
            char_count=s.count(c)
            if char_count > 0:
                # If even counts, minumum length can be 2
                if char_count %2 == 0:
                    min_len += 2
                else:
                # If odd counts, minimum length can be 1
                    min_len += 1
        return min_len
