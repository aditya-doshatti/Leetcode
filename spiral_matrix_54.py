'''
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

https://leetcode.com/problems/spiral-matrix/
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) <1: return []
        if len(matrix) == 1: return matrix[0]
        l = []
        m = len(matrix)
        n = len(matrix[0])
        c=0;
        while(c<(min(m,n)+1)/2):
            for i in range(c,n-c):
                l.append(matrix[c][i])
            for i in range(c+1,m-c-1):
                l.append(matrix[i][n-c-1])
            i = n-c-1
            while m-c-1!=c and i>=c:
                l.append(matrix[m-c-1][i])
                i-=1
            i = m-c-2
            while n-c-1!=c and i>c:
                l.append(matrix[i][c])
                i-=1
            c+=1
        return l
        '''
	My solution works well with Sqaure Matrix
        a,b,c,d = (0,0), (0, len(matrix[0])-1), (len(matrix)-1,0), (len(matrix)-1, len(matrix[0])-1)
        x, minus = False, False
        k = len(matrix) * len(matrix[0])
        i,j =0,0
        retVal = []
        while k > 0:
            print(i,j)
            retVal.append(matrix[i][j])
            if x:
                if minus:
                    i -= 1
                    if i < 0:
                        i = 0
                else:
                    i += 1
                    if i == len(matrix):
                        i -= 1
            else:
                if minus:
                    j -= 1
                    if j < 0:
                        j = 0
                else:
                    j += 1
                    if j == len(matrix[i]):
                        j = j-1
                        i += 1
            if (i,j) == b:
                b = (b[0]+1, b[1]-1)
                x, minus = True, False
            elif (i,j) == d:
                d = (d[0]-1, d[1]-1)
                x, minus = False, True
            elif (i,j) == c:
                c = (c[0]-1, c[1]+1)
                x, minus = True, True
            elif (i,j) == a:
                a = (a[0]+1, a[1]+1)
                i,j = a[0], a[1]
                x, minus = False, False
            k-=1
        return retVal
        '''
                
