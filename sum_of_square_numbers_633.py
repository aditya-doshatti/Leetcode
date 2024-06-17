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
    def judgeSquareSum(self, c: int) -> bool
        i , maxVal = 0, int(math.sqrt(c))
        while i <= maxVal:
            sumVal = i ** 2 + maxVal ** 2
            if sumVal == c:
                return True
            elif sumVal > c:
                maxVal -= 1
            else:
                i += 1
        return False
        '''
        if c == 0:
            return True
        maxVal = c**0.5
        maxVal = maxVal//1
        while maxVal > 0:
            diff = c - (maxVal ** 2)
            # print(diff, diff ** 0.5)
            if (diff ** 0.5) % 1 == 0:
                return True
            maxVal -= 1
        return False
        '''
        '''
        sqrVal = set()
        maxVal = int(math.sqrt(c))
        for i in range(maxVal + 1):
            sqrVal.add(i ** 2)
        for n in sqrVal:
            if c - n in sqrVal:
                return True
        return False
        '''
