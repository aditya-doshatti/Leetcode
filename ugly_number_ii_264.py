'''
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

https://leetcode.com/problems/ugly-number-ii/
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        retlist = [1]
        p2, p3, p5 = 0, 0 , 0
        for i in range(1, n+1):
            minimum = min(retlist[p2]*2, retlist[p3]*3, retlist[p5]*5)
            if minimum == retlist[p2]*2:
                p2 +=1
            if minimum == retlist[p3]*3:
                p3 += 1
            if minimum == retlist[p5]*5:
                p5 += 1
            retlist.append(minimum)
        return retlist[n-1]
