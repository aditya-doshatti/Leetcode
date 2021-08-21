'''
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

https://leetcode.com/problems/valid-sudoku/
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val != '.':
                    if val in rows[i]:
                        return False
                    rows[i].add(val)
                    if val in col[j]:
                        return False
                    col[j].add(val)
                    k = (i//3) * 3 + j//3
                    if val in box[k]:
                        return False
                    box[k].add(val)
        return True
