'''
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, errstack = [], []
        for index,char in enumerate(s):
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    errstack.append((char, index))
            elif char == '(':
                stack.append((char, index))
        while stack:
            ind = stack.pop()[1]
            s = s[:ind] + s[ind + 1:]
        while errstack:
            ind = errstack.pop()[1]
            s = s[:ind] + s[ind + 1:]
        return s
