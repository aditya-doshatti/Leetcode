'''
32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

https://leetcode.com/problems/longest-valid-parentheses/
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lVal, rVal, retVal = 0 , 0 , 0
        for i in range(len(s)):
            if s[i] == "(":
                lVal += 1
            else:
                rVal += 1
            if lVal == rVal:
                retVal = max(retVal, 2*rVal)
            elif rVal >= lVal:
                lVal = rVal = 0
        lVal = rVal = 0
        print(retVal)
        for i in range(len(s)-1, -1 , -1):
            if s[i] == "(":
                lVal += 1
            else:
                
                rVal += 1
            if lVal == rVal:
                retVal = max(retVal, 2*lVal)
            elif lVal >= rVal:
                lVal = rVal = 0
        return retVal
        # retVal,tmp = 0, 0
        # stack = []
        # for i in range(len(s)):
        #     char = s[i]
        #     if char == ")":
        #         if stack:
        #             stack.pop()
        #             tmp += 1
        #         else:
        #             retVal = max(tmp,retVal)
        #             tmp = 0
        #     if char == "(" and i < len(s):
        #         stack.append("(")
        #         tmp += 1
        # retVal = max(retVal, tmp)
        # if stack:
        #     retVal -= len(stack)
        # return retVal
                    
            
