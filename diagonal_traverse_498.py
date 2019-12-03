'''
498. Diagonal Traverse
Medium

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.

https://leetcode.com/problems/diagonal-traverse/
'''
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dic[i+j].append(matrix[i][j])
        flag, retVal = False, []
        for key in dic:
            val = dic[key]
            if flag:
                retVal += val
            else:
                retVal += val[::-1]
            flag = not flag
        return retVal
