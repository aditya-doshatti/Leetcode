'''
402. Remove K Digits
Medium

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

https://leetcode.com/problems/remove-k-digits/
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ''
        if len(num) == k:
            return '0'
        stack = []
        for val in num:
            while k and stack and stack[-1] > val:
                stack.pop()
                k -=1
            stack.append(val)
        while k:
            stack.pop()
            k-=1
        retVal = ''.join(stack)
        if int(retVal) == 0:
            return '0'
        retVal = retVal.lstrip('0')
        return retVal
