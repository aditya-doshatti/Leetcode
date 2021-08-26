'''
633. Sum of Square Numbers
Medium
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

https://leetcode.com/problems/sum-of-square-numbers/
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrVal = set()
        maxVal = int(math.sqrt(c))
        for i in range(maxVal + 1):
            sqrVal.add(i ** 2)
        for n in sqrVal:
            if c - n in sqrVal:
                return True
        return False
