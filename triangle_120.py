'''
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

https://leetcode.com/problems/triangle/
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.retValdic = {}
        def helper(row, column):
            if (row, column) in self.retValdic:
                return self.retValdic[(row, column)]
            if row >= len(triangle):
                return 0
            retVal = triangle[row][column]
            retVal += min(helper(row +1, column),helper(row +1, column + 1))
            self.retValdic[(row, column)] = retVal
            return retVal
        return helper(0,0)
        # TLE
        # retVal = 0
        # self.retValList = []
        # def helper(triangle, row, column, retVal):
        #     if row == len(triangle):
        #         self.retValList.append(retVal)
        #     if row < len(triangle) and column + 1 < len(triangle[row]):
        #         return retVal + min(helper(triangle, row +1, column, retVal + triangle[row][column]),
        #                    helper(triangle, row +1, column + 1, retVal + triangle[row][column + 1]))
        #     return retVal
        # retVal = helper(triangle, 1, 0, triangle[0][0])
        # return min(self.retValList)
                         
