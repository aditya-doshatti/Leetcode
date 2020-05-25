'''
1252. Cells with Odd Values in a Matrix
Easy

Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Example 1:

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
'''
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols, retVal = [0] * n, [0] * m, 0
        for val in indices:
            rows[val[0]] += 1
            cols[val[1]] += 1
        odd_rows = odd_cols = 0
        for row in rows:
            if row % 2 == 1: 
                odd_rows += 1
        for col in cols:
            if col % 2 == 1: 
                odd_cols += 1
        return (odd_rows * (m - odd_cols)) + (odd_cols * (n - odd_rows))
    
        # rows, cols, retVal = [0] * n, [0] * m, 0
        # for val in indices:
        #     rows[val[0]] += 1
        #     cols[val[1]] += 1
        # for i in range(n):
        #     for j in range(m):
        #         if (rows[i] + cols[j]) % 2:
        #             retVal += 1
        # return retVal
