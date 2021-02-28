'''
29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

https://leetcode.com/problems/divide-two-integers/
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag=( (dividend < 0) != (divisor < 0) )
        dividend = left = abs(dividend)
        divisor  = div  = abs(divisor)
        Q = 1
        retVal = 0
        while left >= divisor:
            left -= div
            retVal  += Q 
            Q    += Q
            div  += div
            if left < div:
                div = divisor
                Q = 1
        if flag:
            return max(-retVal, -2147483648)
        else:
            return min(retVal, 2147483647)
        
        
        # #account for Q = 2^31 = -2^31/-1 case (because 2^31 doesn't fit in environment register range)
        # if dividend == -2147483648 and divisor == -1:
        #     return 2147483647
        # if divisor == -2147483648:
        #     if dividend == -2147483648:
        #         return 1
        #     else:
        #         return 0
        # retVal = 0
        # if dividend == divisor:
        #     return 1
        # if divisor == 1:
        #     return dividend
        # if divisor == -1:
        #     return dividend * -1
        # if dividend < 0 and divisor > 0:
        #     dividend *= -1
        #     flag = True
        # elif dividend > 0 and divisor < 0:
        #     divisor *= -1
        #     flag = True
        # elif dividend < 0 and divisor < 0:
        #     dividend *= -1
        #     divisor *= -1
        #     flag = False
        # else:
        #     flag = False
        # while dividend > divisor:
        #     # print(dividend, divisor)
        #     if dividend - divisor >= divisor:
        #         dividend -= divisor
        #         retVal += 1
        #     else:
        #         break
        #     # if divisor + divisor <= dividend:
        #     #     divisor += divisor
        #     #     retVal += 1
        #     # else:
        #     #     break
        # return (retVal  + (dividend > divisor)) * -1 if flag else retVal  + (dividend > divisor)
