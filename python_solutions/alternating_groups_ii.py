class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        len_c = len(colors)
        colors_extended = colors + colors[0:k]
        for left_idx in range(len_c):
            right_idx = left_idx + k
            prev = colors_extended[left_idx]
            alternating = True
            for c_idx in range(left_idx+1, right_idx, 1):
                if prev == colors_extended[c_idx]:
                    alternating = False
                    break
                prev = colors_extended[c_idx]
            if alternating:
                res += 1
        return res
