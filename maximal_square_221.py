'''
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

https://leetcode.com/problems/maximal-square/
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        #dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        retVal = 0
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[i-1])):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) +1
                    retVal = max(retVal, matrix[i][j])
                else:
                    matrix[i][j] = 0
        return retVal**2
#         retVal = 1
#         i = 0
#         while i < len(matrix):
#             j, win = 0, 0
#             while j < len(matrix[i]):
#                 if matrix[i][j] == '1':
#                     win += 1
#                 elif win > 0:
#                     if self.checkWin(i+1, j-1, win, matrix):
#                         print(i, j, win)
#                         retVal = max(retVal, win*win)
#                     win = 0
#                 j +=1
#             if win > 0:
#                 if self.checkWin(i+1, j-1, win, matrix):
#                     print(i, j, win)
#                     retVal = max(retVal, win*win)
#                 win = 0
#             i+=1
#         return retVal

#     def checkWin(self, i , j ,win, matrix):
#         print("in ", i, j, win)
#         if i >= len(matrix):
#             return False
#         else:
#             m = i
#             while m < len(matrix):
#                 n = j
#                 while n > win:
#                     if matrix[m][n] != '1':
#                         return False
#                     n -=1
#                 m+=1
#             return True
