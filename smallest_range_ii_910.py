'''
910. Smallest Range II
Medium

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

https://leetcode.com/problems/smallest-range-ii/
'''
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        minA, maxA = A[0], A[-1]
        retVal = maxA - minA
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            retVal = min(retVal, max(maxA-K, a+K) - min(minA+K, b-K))
        return retVal
