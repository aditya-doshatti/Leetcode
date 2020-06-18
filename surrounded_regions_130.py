'''
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

https://leetcode.com/problems/surrounded-regions/
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        q = collections.deque()

        for i in range(len(board)):
            if board[i][0] == 'O':
                board[i][0] = 'V'
                q.append((i, 0))
            if board[i][len(board[0])-1] == 'O':
                board[i][len(board[0])-1] = 'V'
                q.append((i, len(board[0])-1))

        for j in range(1, len(board[0])-1):
            if board[0][j] == 'O':
                board[0][j] = 'V'
                q.append((0, j))
            if board[len(board)-1][j] == 'O':
                board[len(board)-1][j] = 'V'
                q.append((len(board)-1, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and \
                   board[x][y] == 'O':
                    board[x][y] = 'V'
                    q.append((x, y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == 'O':
    #                 if i-1 >= 0 and j -1 >= 0 and i+1<len(board) and j+1 < len(board[0]) :
    #                     if self.isSurrounded(i,j, board):
    #                         board[i][j] = 'X'
    # def isSurrounded(self, i,j, board):
    #     if board[i][j+1] == 'O':
    #         if i-1 >= 0 and j >= 0 and i+1<len(board) and j+2 < len(board[0]) :
    #             board[i][j] = 'X'
    #             if not self.isSurrounded(i, j+1, board):
    #                 board[i][j] == 'O'
    #     if board[i][j-1] == 'O':
    #         if i-1 >= 0 and j-2 >= 0 and i+1<len(board) and j < len(board[0]) :
    #             board[i][j] = 'X'
    #             if not self.isSurrounded(i, j-1, board):
    #                 board[i][j] == 'O'
    #     if board[i+1][j] == 'O':
    #         if i >= 0 and j >= 0 and i+2<len(board) and j+1 < len(board[0]) :
    #             board[i][j] = 'X'
    #             if not self.isSurrounded(i+1, j, board):
    #                 board[i][j] == 'O'
    #     if board[i-1][j] == 'O':
    #         if i-2 >= 0 and j >= 0 and i<len(board) and j+1 < len(board[0]) :
    #             board[i][j] = 'X'
    #             if not self.isSurrounded(i-1, j, board):
    #                 board[i][j] == 'O'
    #     return board[i][j+1] == 'X' and board[i][j-1] == 'X' and board[i-1][j] == 'X' and board[i+1][j] == 'X'
