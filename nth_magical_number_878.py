'''
878. Nth Magical Number
Hard

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2

https://leetcode.com/problems/nth-magical-number/
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = a / gcd(a,b) * b
        def magic_below_x(x):
            # How many magical numbers are <= x?
            return x // a + x // b - x // lcm

        lo = 0
        hi = n * min(a, b)
        while lo < hi:
            mi = (lo + hi) // 2
            if magic_below_x(mi) < n:
                lo = mi + 1
            else:
                hi = mi
        return lo % (10**9 + 7)
