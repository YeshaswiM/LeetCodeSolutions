from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Slightly better, maintain 2 arrays to track if a row or column needs to be toggled to 0
        width = len(matrix[0])
        height = len(matrix)
        rows = columns = []
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    columns.append(i)
                    rows.append(j)
        for i in range(height):
            if i in columns:
                for j in range(width):
                    matrix[i][j] = 0
            else:
                for j in rows:
                        matrix[i][j] = 0
        # Return for testing
        return matrix
