from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        width = len(grid) - 1
        height = len(grid[0]) - 1
        # Traverse the grid and check for neighbors
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # If land, add 4
                    peri_add = 4
                    # If another land is on the left, subtract 1
                    if i > 0 and grid[i-1][j] == 1:
                            perct -= 1
                    # If another land is on the right, subtract 1
                    if i < width and grid[i + 1][j] == 1:
                            perct -= 1
                    # If another land is below, subtract 1
                    if j > 0 and grid[i][j - 1] == 1:
                            perct -= 1
                    # If another land is above, subtract 1
                    if j < height and grid[i][j + 1] == 1:
                            perct -= 1
                    perimeter += peri_add
        return perimeter


        