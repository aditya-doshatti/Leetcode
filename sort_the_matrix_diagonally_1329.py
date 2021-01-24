'''
1329. Sort the Matrix Diagonally
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

https://leetcode.com/problems/sort-the-matrix-diagonally/
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heappush(d[i-j], mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = heappop(d[i-j])       
        return mat
        # m, n = len(mat), len(mat[0])
        # maxDiff = max(m, n)
        # diff = 0
        # while diff < maxDiff:
        #     print(mat)
        #     i, j = 0, 0
        #     arr = []
        #     if diff == 0:
        #         while i < m and j < n:
        #             j += diff
        #             arr.append(mat[i][j])
        #             i += 1
        #             j += 1
        #         arr.sort()
        #         i, j = 0, 0
        #         k = 0
        #         while i < m and j < n:
        #             j += diff
        #             mat[i][j] = arr[k]
        #             i += 1
        #             j += 1
        #             k += 1
        #     else:
        #         while i < m and j < n:
        #             i += diff
        #             arr.append(mat[i][j])
        #             i += 1
        #             j += 1
        #         arr.sort()
        #         i, j = 0, 0
        #         k = 0
        #         while i < m and j < n:
        #             i += diff
        #             mat[i][j] = arr[k]
        #             i += 1
        #             j += 1
        #             k += 1
        #         i, j = 0
        #         arr = []
        #         while i < m and j < n:
        #             j += diff
        #             arr.append(mat[i][j])
        #             i += 1
        #             j += 1
        #         arr.sort()
        #         i, j = 0, 0
        #         k = 0
        #         while i < m and j < n:
        #             j += diff
        #             mat[i][j] = arr[k]
        #             i += 1
        #             j += 1
        #             k += 1
        #     diff += 1
        # return mat
            
