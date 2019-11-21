'''
1037. Valid Boomerang
Easy

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true

https://leetcode.com/problems/valid-boomerang/
'''
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points[1][0] != points[0][0]:
            m1 = float(points[1][1] - points[0][1])/(points[1][0]-points[0][0])
        elif points[1][1] == points[0][1]:
            return False
        else:
            m1 = "undef"
        if points[2][0] != points[1][0]:
            m2 = float(points[2][1] - points[1][1])/(points[2][0]-points[1][0])
        elif points[2][0] == points[0][0] or points[2][1] == points[1][1]:
            return False
        else:
            m2 = "undef"
        print m1,m2
        return not m1 == m2
