'''
1253. Reconstruct a 2-Row Binary Matrix
Medium


The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

 

Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/submissions/
'''
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        retVal, i =[[0]*len(colsum),[0]*len(colsum)], 0
        if sum(colsum) != upper + lower:
            return []
        while i < len(colsum):
            if colsum[i] == 0:
                i+=1
                continue
            elif colsum[i] == 2:
                retVal[0][i] = 1
                retVal[1][i] = 1
                upper -=1
                lower -=1
            else:
                if upper > lower:
                    retVal[0][i] = 1
                    upper -=1
                else:
                    retVal[1][i] = 1
                    lower-=1
            i+=1
        if upper !=0 or lower!=0:
            return []
        return retVal
