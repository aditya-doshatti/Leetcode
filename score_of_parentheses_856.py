'''
856. Score of Parentheses
Medium

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1

https://leetcode.com/problems/score-of-parentheses/
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()
