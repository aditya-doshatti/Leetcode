'''
1380. Lucky Numbers in a Matrix

Easy

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

https://leetcode.com/problems/lucky-numbers-in-a-matrix/description
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        retVal = []
        maxCol = []
        m = len(matrix)
        n = len(matrix[0])
        for c in range(n):
            maxCol.append(max(matrix[r][c] for r in range(m)))
        for r in range(m):
            minVal = min(matrix[r])
            minIndex = matrix[r].index(minVal)
            if minVal == maxCol[minIndex]:
                retVal.append(minVal)
        return retVal
