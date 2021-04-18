'''
1074. Number of Submatrices That Sum to Target
Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
'''
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        dp, retVal = {}, 0
        for k in range(len(matrix)):
            temp = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(len(matrix[0])+1), 2):
                dp[i, j, k] = dp.get((i,j,k-1), 0) + temp[j] - temp[i]
        for i, j in combinations(range(len(matrix[0])+1), 2):
            Temp = Counter([0])
            for k in range(len(matrix)):
                retVal += Temp[dp[i, j, k] - target]
                Temp[dp[i, j, k]] += 1
        return retVal
