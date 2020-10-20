'''
1007. Minimum Domino Rotations For Equal Row
Medium

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
'''
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in range(1, 7):
            if all(x == a or x == b for a, b in zip(A, B)):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1
