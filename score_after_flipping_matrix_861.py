'''
861. Score After Flipping Matrix

Medium

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).


Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

https://leetcode.com/problems/score-after-flipping-matrix/description/
'''
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                self.flip(grid,i, -1)
        
        for i in range(len(grid[0])):
            ones, zeros = 0, 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    zeros += 1
                else:
                    ones += 1
            if zeros > ones:
                self.flip(grid, -1, i)
        sumVal = 0
        matrix_strings = [''.join(str(cell) for cell in row) for row in grid]
        for string in matrix_strings:
            sumVal += int(string, 2)
        return sumVal

    def flip(self, grid, row, col):
        if row != -1:
            for i in range(len(grid[row])):
                if grid[row][i] == 1:
                    grid[row][i] = 0
                else:
                    grid[row][i] = 1
        elif col != -1:
            for i in range(len(grid)):
                if grid[i][col] == 1:
                    grid[i][col] = 0
                else:
                    grid[i][col] = 1
