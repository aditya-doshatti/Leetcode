'''
668. Kth Smallest Number in Multiplication Table
Hard

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k
        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
