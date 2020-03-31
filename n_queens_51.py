'''
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

https://leetcode.com/problems/n-queens/
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
	#Copied solution
        position_in_row = [-1] * n
        column = [True] * n
        left_diagonal = [True] * (2 * n - 1)
        right_diagonal = [True] * (2 * n - 1)
        outputs = []
        def putQueen(row):
            for col in range(n):
                if column[col] and left_diagonal[row + col] and right_diagonal[row + n - col - 1]:
                    position_in_row[row] = col
                    column[col] = left_diagonal[row + col] = right_diagonal[row + n - col - 1] = False
                    if row < n - 1:
                        putQueen(row + 1)
                    else:
                        output = []
                        for row in range(n):
                            output.append('.' * position_in_row[row] + 'Q' + '.' * (n - position_in_row[row] - 1))
                        outputs.append(output)
                    column[col] = left_diagonal[row + col] = right_diagonal[row + n - col - 1] = True
        putQueen(0)
        return outputs
        # stack, res = [[(0, i)] for i in range(n)], []
        # while stack:
        #     board = stack.pop()
        #     row = len(board)
        #     if row == n:
        #         res.append([''.join('Q' if i == c else '.' for i in range(n))
        #                     for r, c in board])
        #     for col in range(n):
        #         if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
        #             stack.append(board+[(row, col)])
        # return res
# My Solution
#     def __init__(self):
#         self.n = 0
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         self.n = n
#         retVal = []
#         col = set()
#         for i in range(n-1):
#             print(col)
#             board = [['.' for _ in range(n)] for _ in range(n)]
#             if self.reccursive(board, i):
#                 if not board[0].index('Q') in col:
#                     retVal.append(board)
#                     col.add( board[0].index('Q') )
#         return retVal
        
#     def reccursive(self, board, column):
#         if column >= self.n:
#             return True
#         for i in range(self.n):
#             if self.checkCorrect(i, column, board):
#                 board[i][column] = 'Q'
#                 if self.reccursive(board, column+1):
#                     return True
#                 board[i][column] = '.'
#         return False
        
#         # i, j, prev = 0, 0, (float('inf'), float('inf'))
#         # while n>0:
#         #     if self.checkCorrect(i, j, board):
#         #         board[i][j] = 'Q'
#         #         prev = (i, j)
#         #         i +=1
#         #         j +=2
#         #         n -= 1
#         #     else:
#         #         if prev[0] != float('inf'):
#         #             print(prev, i, j)
#         #             a = prev[0]
#         #             b = prev[1]                        
#         #             board[a][b] = '.'
#         #             n+=1
#         #             if a == i and b == j-1:
#         #                 i -=1
#         #                 j = i+1
#         #             else:
#         #                 i = a
#         #                 j = b+1
#         #                 if j >= len(board[i]):
#         #                     j = 0
#         #         else:
#         #             j +=1
#         # for k in range(len(board)):
#         #     board[k] = ''.join(board[k])
#         # return board
            
        
#     def checkCorrect(self, row, col, board):
#         #print(i, j)
#         for a in range(col):
#             if board[row][a] == 'Q':
#                 return False
#         # a, b = i, j
#         # Check upper diagonal on left side 
#         for i, j in zip(range(row, -1, -1),  
#                         range(col, -1, -1)): 
#             if board[i][j] == 'Q': 
#                 return False

#         # Check lower diagonal on left side 
#         for i, j in zip(range(row, self.n, 1),  
#                         range(col, -1, -1)): 
#             if board[i][j] == 'Q': 
#                 return False
#         # while a < self.n and b >= 0:
#         #     if board[i][j] == 'Q':
#         #         return False
#         #     a += 1
#         #     b -= 1
#         # a, b = i, j
#         # while a >= 0 and b >= 0:
#         #     if board[i][j] == 'Q':
#         #         return False
#         #     a -= 1
#         #     b -= 1
#         return True
        
#         # print(i, j)
#         # if i < len(board) and j < len(board[i]):
#         #     a, b = i, j+1
#         #     while b < len(board[a]):
#         #         if board[a][b] == 'Q':
#         #             return False
#         #         b += 1
#         #     a, b = i+1, j
#         #     while a < len(board):
#         #         if board[a][b] == 'Q':
#         #             return False
#         #         a += 1
#         #     a,b = i+1, j+1
#         #     while a+1 < len(board) and b+1 <len(board[a]):
#         #         if board[a+1][b+1] == 'Q':
#         #             return False
#         #         a += 1
#         #         b += 1 
#         #     return True
#         # else:
#         #     return False
#     def isSafe(self, board, row, col): 
#         # Check this row on left side 
#         for i in range(col): 
#             if board[row][i] == 'Q': 
#                 return False

#         # Check upper diagonal on left side 
#         for i, j in zip(range(row, -1, -1),  
#                         range(col, -1, -1)): 
#             print(i, j)
#             if board[i][j] == 'Q': 
#                 return False

#         # Check lower diagonal on left side 
#         for i, j in zip(range(row, self.n, 1),  
#                         range(col, -1, -1)): 
#             if board[i][j] == 'Q': 
#                 return False

#         return True
