'''
59. Spiral Matrix II
Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

https://leetcode.com/problems/spiral-matrix-ii/
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        retVal = [[None] * n for _ in range(n)]
        x, y = 0, 0
        for i in range(1, n * n + 1):
            retVal[x][y] = i
            a, b = steps[direction]
            if not (n > x + a >= 0 <= y + b < n and not retVal[x + a][y + b]):
                direction = (direction + 1) % 4
                a, b = steps[direction]
            x = x + a
            y = y + b
        return retVal
