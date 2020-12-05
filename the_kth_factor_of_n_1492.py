'''
1492. The kth Factor of n
Medium

Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

https://leetcode.com/problems/the-kth-factor-of-n/
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 1
        if k == 1:
            return 1
        if k > n:
            return -1
        for i in range(2, n+1):
            if n % i == 0:
                counter += 1
            if counter == k:
                return i
        return -1
