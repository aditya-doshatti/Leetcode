'''
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

https://leetcode.com/problems/valid-perfect-square/
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l, r = 2, num//2
        while l <= r:
            mid = (l+r)//2
            curr = mid*mid
            if curr == num:
                return True
            elif curr > num:
                r = mid-1
            else:
                l = mid+1
        return False
        # val = 1
        # while val*val <= num:
        #     if val*val == num:
        #         return True
        #     else:
        #         val +=1
        # return False
