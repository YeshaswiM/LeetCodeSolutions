class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Most recolors can be k, so start with that
        min_recolor = k
        for left_idx in range(len(blocks)):
            right_idx = left_idx + k
            if right_idx > len(blocks): 
                break # Exit if we go out of bounds
            # Count the number of white blocks in the current window
            recolor = blocks[left_idx:right_idx].count("W")
            # Update the minimum recolor count
            min_recolor = min(min_recolor, recolor)
            # If we find 0, we break early, can't do better than that
            if min_recolor == 0: 
                break
        return min_recolor
