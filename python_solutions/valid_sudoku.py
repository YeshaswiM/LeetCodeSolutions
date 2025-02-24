from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            # Checking all rows
            arr = []
            for j in range(len(board[0])):
                # print(arr, board[i][j])
                if board[i][j] != "." and board[i][j] not in arr:
                    arr.append(board[i][j])
                elif board[i][j] != "." and board[i][j] in arr:
                    return False
        
        for j in range(len(board[0])):
            # Checking all columns
            arr = []
            for i in range(len(board)):
                if board[i][j] != "." and board[i][j] not in arr:
                    arr.append(board[i][j])
                elif board[i][j] != "." and board[i][j] in arr:
                    return False
        # Checking each 3x3 box of the sudoku
        box_starts = [(0,0),(0,3),(0,6),
                        (3,0),(3,3),(3,6),
                        (6,0),(6,3),(6,6)]
        for si, sj in box_starts:
            arr = []
            for i in [si, si+1, si+2]:
                for j in [sj, sj+1, sj+2]:
                    if board[i][j] != "." and board[i][j] not in arr:
                        arr.append(board[i][j])
                    elif board[i][j] != "." and board[i][j] in arr:
                        return False
        return True
