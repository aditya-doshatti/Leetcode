'''
980. Unique Paths III
Hard

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

https://leetcode.com/problems/unique-paths-iii/
'''
class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        self.retVal = 0
        empty = 1
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] >= 0): 
                return
            if A[x][y] == 2:
                self.retVal += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x, y, empty)
        return self.retVal
