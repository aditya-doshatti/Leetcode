'''
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

https://leetcode.com/problems/search-a-2d-matrix-ii/
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i , j = 0 , len(matrix[0]) - 1
        while i < len(matrix) and j >=0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False
