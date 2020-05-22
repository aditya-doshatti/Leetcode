'''
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

https://leetcode.com/problems/count-square-submatrices-with-all-ones/
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        retVal = 0
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            retVal += matrix[i][0]
        for i in range(1,m):
            retVal += matrix[0][i]
        for i in range(1,n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
                    retVal += matrix[i][j]
        return retVal
