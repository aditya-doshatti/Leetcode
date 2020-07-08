'''
463. Island Perimeter
Easy

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

https://leetcode.com/problems/island-perimeter/
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        retVal = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    retVal += 4
                    if i > 0 and grid[i-1][j] == 1:
                        retVal -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        retVal -= 2
        return retVal

    #     self.retVal = 0
    #     visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j]:
    #                 self.dfs(i, j, grid, visited)
    #     return self.retVal
    #
    # def dfs(self, i, j, grid, visited):
    #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
    #         self.retVal += 1
    #         return
    #     if visited[i][j]:
    #         return
    #     else:
    #         if grid[i][j] == 1:
    #             visited[i][j] = 1
    #             for val in [(-1,0),(1,0),(0,-1),(0,-1)]:
    #                 self.dfs(i+val[0], j + val[1], grid, visited) 
    #         else:
    #             self.retVal += 1
            
            
