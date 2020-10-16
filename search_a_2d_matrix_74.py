'''
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

https://leetcode.com/problems/search-a-2d-matrix/
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rowBeg, colBeg, rowEnd, colEnd = 0, 0, len(matrix)-1, len(matrix[0])-1
        while rowBeg <= rowEnd:
            if matrix[rowBeg][colBeg] <=target <=matrix[rowBeg][colEnd]:
                return self.binarySearch(matrix[rowBeg], target)
            else:
                mid = (rowBeg + rowEnd)// 2
                if matrix[mid][colBeg] <=target <=matrix[mid][colEnd]:
                    return self.binarySearch(matrix[mid], target)
                elif target >matrix[mid][colBeg]:
                    rowBeg = mid + 1
                else:
                    rowEnd = mid - 1
    
    def binarySearch(self, nums, target):
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        return False                
