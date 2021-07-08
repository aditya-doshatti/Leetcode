'''
378. Kth Smallest Element in a Sorted Matrix
Medium

4146

201

Add to List

Share
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) 
        def countLessOrEqual(x):
            cnt = 0
            c = n - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                cnt += (c + 1)
            return cnt
        left, right = matrix[0][0], matrix[-1][-1]
        retVal = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                retVal = mid
                right = mid - 1
            else:
                left = mid + 1
        return retVal
