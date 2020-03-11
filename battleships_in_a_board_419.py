'''
419. Battleships in a Board
Medium

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.

https://leetcode.com/problems/battleships-in-a-board/
'''
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        elif len(board) ==1 and len(board[0]) ==1:
            if board[0][0] == 'X':
                return 1
            else:
                return 0
        else:
            a, b, retVal = len(board), len(board[0]), 0
            for i in range(a):
                for j in range(b):
                    if board[i][j] != 'X': continue
                    if i > 0 and board[i-1][j] == 'X': continue
                    if j > 0 and board[i][j-1] == 'X': continue
                    retVal += 1
            return retVal
        # row, col = -1, {}
        # for i in range(len(board)):
        #     if board[i].count('X') > 1:
        #         row = i
        #     elif board[i].count('X') == 1:
        #         col[board[i].index('X')] = col.get(board[i].index('X'),0) +1
        # finalCol, finaVal = -1, -1
        # for c,v in col.items():
        #     if v > finaVal:
        #         finalV = v
        #         finalCol = c
        # retVal = 0
        # for i in range(len(board)):
        #     if i == row:
        #         for j in range(len(board[i])):
        #             if board[i][j] == 'X':
        #                 if j > 0 and j < len(board[i])-2:
        #                     if board[i][j-1] != 'X' and board[i][j+1] != 'X':
        #                         retVal +=1
        #                 elif j > 0 and board[i][j-1] != 'X':
        #                         retVal +=1
        #                 elif j < len(board[i])-2 and board[i][j+1] != 'X':
        #                     retVal += 1
        #     elif finalCol != -1:
        #         if board[i][finalCol] == 'X':
        #             if i > 0 and i < len(board)-2:
        #                 if board[i-1][finalCol] != 'X' and board[i+1][finalCol] != 'X':
        #                     retVal +=1
        #             elif i > 0 and board[i-1][finalCol] != 'X':
        #                     retVal +=1
        #             elif i < len(board[i])-2 and board[i+1][finalCol] != 'X':
        #                 retVal += 1
        # return retVal
                            
                            
            
