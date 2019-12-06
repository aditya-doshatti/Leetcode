'''
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

https://leetcode.com/problems/search-a-2d-matrix-ii/
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix[0]):
            return False
        i,j = len(matrix)-1, 0
        while i >=0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
        # if not matrix:
        #     return False
        # i, j, mid = 0, 0 ,0
        # while True:
        #     if matrix[i][j] == target:
        #         return True
        #     if target < matrix[i][j]:
        #         return False
        #     if target > matrix[i][len(matrix[i])-1]:
        #         j = len(matrix[i])
        #     else:
        #         mid = (i+len(matrix[i])-1)//2
        #         if target == matrix[i][mid]:
        #             return True
        #         if target < matrix[i][mid]:
        #             j = mid-1
        #         else:
        #             j = mid + 1
