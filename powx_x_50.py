'''
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

https://leetcode.com/problems/powx-n/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/(self.myPow(x,-n))
        elif n > 0:
            if n % 2:
                val = self.myPow(x, (n-1)/2)
                return val * val * x
            else:
                val = self.myPow(x, n/2)
                return val * val
