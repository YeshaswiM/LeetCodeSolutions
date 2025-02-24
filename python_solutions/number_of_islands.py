from typing import List

class Solution:
    def findNeighbors(self, grid, i, j):
        grid[i][j] = "-1"
        if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
                self.findNeighbors(grid, i, j+1)
        if i < len(grid) - 1 and grid[i+1][j] == "1":
                self.findNeighbors(grid, i+1, j)
        if j > 0 and grid[i][j-1] == "1":
                self.findNeighbors(grid, i, j-1)
        if i > 0 and grid[i-1][j] == "1":
                self.findNeighbors(grid, i-1, j)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        num_islands = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.findNeighbors(grid,i,j)
        return num_islands
