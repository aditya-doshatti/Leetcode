'''
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

https://leetcode.com/problems/number-of-islands/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        retVal= 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, visited)
                    retVal += 1
        return retVal
    
    def dfs(self, i , j ,grid, visited):
        if 0<= i < len(grid) and 0 <= j < len(grid[i]):
            if visited[i][j] == True:
                return
            visited[i][j] = True
            if grid[i][j] == '1':
                self.dfs(i-1, j, grid, visited)
                self.dfs(i+1, j, grid, visited)
                self.dfs(i, j-1, grid, visited)
                self.dfs(i, j+1, grid, visited)
        return
                
                
