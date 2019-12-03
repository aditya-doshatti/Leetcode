'''
289. Game of Life
Medium

1260

227

Favorite

Share
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

https://leetcode.com/problems/game-of-life/
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        change = []
        check = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                for c in check:
                    i1 = (i + c[0])
                    j1 = (j + c[1])
                    if (i1 < len(board) and i1 >= 0) and (j1 < len(board[0]) and j1 >= 0) and board[i1][j1] == 1:
                        count += 1
                # if i == 0 and j == 0:
                #     count = count + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
                # elif i ==0 and j < len(board[i])-1:
                #     count = count + board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i-1][j-1] + board[i+1][j]
                # elif i == 0 and j == len(board[i]) -1:
                #     count = count + board[i+1][j] + board[i][j-1] + board[i+1][j-1]
                # elif i == len(board)-1 and j == 0:
                #     count = count + board[i-1][j] + board[i][j+1] + board[i-1][j+1]
                # elif i == len(board)-1 and j < len(board[i])-1:
                #     count = count + board[i-1][j] + board[i][j+1] + board[i-1][j+1] + board[i-1][j-1] + board[i][j-1] 
                # elif i == len(board)-1 and j == len(board[i])-1:
                #     count = count + board[i-1][j] + board[i][j-1] + board[i-1][j-1]
                # elif j == 0:
                #     count = count + board[i-1][j] + board[i][j+1] + board[i-1][j+1] + board[i+1][j+1] + board[i+1][j]
                # elif j == len(board[i])-1:
                #     count = count + board[i-1][j] + board[i][j-1] + board[i-1][j-1] + board[i+1][j-1] + board[i+1][j]
                # else:
                #     count = count + board[i-1][j] + board[i][j-1] + board[i-1][j-1] + board[i+1][j-1] + board[i+1][j] + board[i][j+1] + board[i-1][j+1] + board[i+1][j+1]
                if board[i][j] == 0 and count == 3:
                    change.append((i,j))
                elif board[i][j] == 1 and (count < 2 or count > 3):
                    change.append((i,j))
        for val in change:
            if board[val[0]][val[1]]:
                board[val[0]][val[1]] = 0
            else:
                board[val[0]][val[1]] = 1
