'''
1137. N-th Tribonacci Number
Easy

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

https://leetcode.com/problems/n-th-tribonacci-number/
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        i, j, k = 0, 1, 1
        for a in range(n - 2):
            i, j, k = j, k , i + j + k
        return k
        # TLE
        # if n == 0:
        #     return 0
        # if n <=2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
