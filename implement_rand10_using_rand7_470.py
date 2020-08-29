'''
470. Implement Rand10() Using Rand7()
Medium

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]

https://leetcode.com/problems/implement-rand10-using-rand7/
'''
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        retVal = 40
        while retVal>=40:
            retVal=(rand7()-1)*7+rand7()-1
        return retVal%10+1
        # k = rand7()
        # retVal = k + (k % 3)
        # return retVal
