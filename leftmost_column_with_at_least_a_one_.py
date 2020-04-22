'''
Leftmost Column with at Least a One
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

Example 1:

Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:
 
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/
'''
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n = binaryMatrix.dimensions()
        row, retVal, flag = 0, n-1, False
        while row < m:
            if n == 0 and flag:
                return n
            if binaryMatrix.get(row, n-1):
                flag = True
                retVal = n-1
                n -= 1
            else:
                row += 1
        if flag:
            return retVal
        return -1
        # found, flag = n-1, False
        # for i in range(m):
        #     prev, end = 0, found
        #     while end >= prev:  
        #         mid = prev + (end-prev) // 2
        #         if binaryMatrix.get(i, mid):
        #             found = min(mid, found)
        #             end = mid - 1
        #             flag = True
        #         else:
        #             prev = mid + 1
        # if flag:
        #     return found
        # return -1
