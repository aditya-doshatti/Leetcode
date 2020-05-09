'''
1232. Check If It Is a Straight Line
Easy

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

https://leetcode.com/problems/check-if-it-is-a-straight-line/
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            slope = (coordinates[-1][1] - coordinates[0][1])/(coordinates[-1][0] - coordinates[0][0])
        except:
            return False
        for point in coordinates:
            if (point[1] - coordinates[0][1]) == slope * (point[0] - coordinates[0][0]):
                continue
            else:
                return False
        return True
        # try:
        #     slope = (coordinates[-1][1] - coordinates[0][1])/(coordinates[-1][0] - coordinates[0][0])
        # except:
        #     return False
        # intercept = (-1 * ( slope * coordinates[0][0])) + coordinates[0][1]
        # for point in coordinates:
        #     if (slope * point[0]) + intercept == point[1]:
        #         continue
        #     else:
        #         return False
        # return True
