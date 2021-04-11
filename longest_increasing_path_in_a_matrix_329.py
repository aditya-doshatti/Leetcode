'''
329. Longest Increasing Path in a Matrix
Hard

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        retVal = 0
        m = len(matrix)
        n = len(matrix[0])
        def helper(i, j, prevVal=-1, visited=[]):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prevVal or (i, j) in visited:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            maxVal = 0
            for dirx, diry in dirs:
                maxVal = max(maxVal, 1+helper(i+dirx, j+diry, matrix[i][j], visited + [(i, j)]))
            dp[(i, j)] = maxVal
            return maxVal
        dp = {}
        for x in range(m):
            for y in range(n):
                retVal = max(retVal, helper(x, y))
        return retVal
