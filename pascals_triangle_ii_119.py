'''
119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

https://leetcode.com/problems/pascals-triangle-ii/
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        retVal = [1,1]
        for i in range(2, rowIndex+1):
            curr = [1]
            for j in range(1,len(retVal)):
                curr.append(retVal[j-1] + retVal[j])
            curr.append(1)
            retVal = curr
        return retVal
