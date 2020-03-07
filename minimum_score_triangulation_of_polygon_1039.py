'''
1039. Minimum Score Triangulation of Polygon
Medium

Share
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
'''
class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = [[0] * len(A) for i in xrange(len(A))]
        for point in xrange(2, len(A)):
            for i in xrange(len(A) - point):
                j = i + point
                arr[i][j] = min(arr[i][k] + arr[k][j] + A[i] * A[j] * A[k] for k in xrange(i + 1, j))
        return arr[0][len(A) - 1]
        # retVal = []
        # for i in range(len(A)):
        #     minus = False
        #     if i == len(A)-1:
        #         if A[i-1] < A[0]:
        #             sec= A[i-1]
        #             minus = True
        #         else:
        #             sec = A[0]
        #         tempsec = sec
        #         sec = sec * A[i]
        #         if minus:
        #             third = min(A[:i-2])
        #         else:
        #             third = min(A[1:i])
        #     else:
        #         if A[i-1] < A[i+1]:
        #             sec= A[i-1]
        #             minus = True
        #         else:
        #             sec = A[i+1]
        #         tempsec = sec
        #         sec = sec * A[i]
        #         if minus:
        #             if i ==0:
        #                 third =  min(A[i+1:i-1])
        #             else:
        #                 third = min(A[:i-1] + A[i+1:])
        #         else:
        #             third = min(A[:i] + A[i+2:])
        #     print(A[i], tempsec, third)
        #     retVal.append(sec * third)
        #     print(retVal)
        # return retVal
            
            
