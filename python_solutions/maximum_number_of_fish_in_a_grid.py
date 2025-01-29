from typing import List

class Solution:
    def __init__(self):
        # track tuples of indexes already visited
        self.visited = []
    def findFish(self, grid: List[List[int]], r: int, c: int) -> int:
        # Recursive function to calculate neighboring fish count
        self.visited.append((r,c))
        fishct = grid[r][c]
        if c < (len(grid[0]) - 1) and grid[r][c + 1] > 0 and (r,c+1) not in self.visited:
            fishct += self.findFish(grid, r, c + 1)
        if  r < (len(grid) - 1) and grid[r + 1][c] > 0 and (r+1,c) not in self.visited:
            fishct += self.findFish(grid, r + 1, c)
        if c > 0 and grid[r][c - 1] > 0 and (r, c-1) not in self.visited:
            fishct += self.findFish(grid, r, c - 1)
        if  r > 0 and grid[r - 1][c] > 0 and (r - 1, c) not in self.visited:
            fishct += self.findFish(grid, r - 1, c)
        return fishct


    def findMaxFish(self, grid: List[List[int]]) -> int:
        rowct = len(grid)
        colct = len(grid[0])
        max_fish = 0
        for i in range(rowct):
            if grid[i].count(0) < colct:
                for j in range(colct):
                    if grid[i][j] > 0:
                        if (i,j) in self.visited: 
                            continue
                        fishes = self.findFish(grid, i, j)
                        max_fish = max(max_fish, fishes)
        return max_fish
