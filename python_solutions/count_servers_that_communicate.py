from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            sumrow = sum(grid[i])
            # If there are more than 1 '1's in the row, add their counts
            if sumrow > 1:
                count += sumrow
            elif sumrow == 1:
                # If only single '1' in row, check respective columns for other '1's
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        column_elements = [g[j] for g in grid]
                        if sum(column_elements)>1:
                            count += 1
        return count
