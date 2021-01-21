'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true

https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in brackets:
                stack.append(char)
                continue
            if not stack:
                return False
            b = stack.pop()
            if char != brackets[b]:
                return False
        return not stack
        # openB = {"(": 0, "{": 1, "[": 2}
        # closeB = {")": 0, "}": 1, "]": 2}
        # for char in s:
        #     if char in openB:
        #         stack.append(char)
        #     elif char in closeB:
        #         if not stack:
        #             return False
        #         if closeB[char] != openB[stack[-1]]:
        #             return False
        #         else:
        #             stack.pop()
        # if stack:
        #     return False
        # return True
