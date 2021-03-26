'''
417. Pacific Atlantic Water Flow
Medium

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

https://leetcode.com/problems/pacific-atlantic-water-flow/
'''
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(x, y, visited):
            if (y, x) in visited:   
                return
            visited.add( (y, x) )
            for dx, dy in ( (-1, 0), (1, 0), (0, 1), (0, -1) ):
                next_x, next_y = x + dx, y + dy
                if not in_valid_range(next_x, next_y):
                    continue
                if matrix[y][x] <= matrix[next_y][next_x]:
                    dfs(next_x, next_y, visited)
        if (not matrix) or (not matrix[0]):
            return []
        h, w = len(matrix), len(matrix[0])
        in_valid_range = lambda x, y: ( 0 <= x < w ) and ( 0 <= y < h )
        possible_pacific, possible_atlantic = set(), set()
        for y in range(h):
            dfs(0, y, possible_pacific)
            dfs(w-1, y, possible_atlantic)
        for x in range(w):
            dfs(x, 0, possible_pacific)
            dfs(x, h-1, possible_atlantic)
        return [ *(possible_pacific & possible_atlantic) ]

        # retVal = []
        # visited = set()
        # def dfs(matrix, x, y):
        #     if (x,y) not in visited:
        #         visited.add((x, y))
        #         print(x, y)
        #         if x > len(matrix)-1 or y > len(matrix)-1:
        #             return True, "A"
        #         if x < 0 or y < 0:
        #             return True, "P"
        #         A, P = False, False
        #         ret, val = dfs(matrix, x-1, y)
        #         if ret:
        #             if not P:
        #                 P = True if val == "P" else False
        #             if not A:
        #                 A = True if val == "A" else False
        #         ret, val = dfs(matrix, x+1, y)
        #         if ret:
        #             if not P:
        #                 P = True if val == "P" else False
        #             if not A:
        #                 A = True if val == "A" else False
        #         ret, val = dfs(matrix, x, y-1)
        #         if ret:
        #             if not P:
        #                 P = True if val == "P" else False
        #             if not A:
        #                 A = True if val == "A" else False
        #         ret, val = dfs(matrix, x, y+1)
        #         if ret:
        #             if not P:
        #                 P = True if val == "P" else False
        #             if not A:
        #                 A = True if val == "A" else False
        #         if A and P:
        #             retVal.append([x, y])
        #         print(x,y, A, P)
        #     return None, None
        # dfs(matrix, 0, 0)
        # print(visited)
        # return retVal
                    
            
