'''
678. Valid Parenthesis String
Medium

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True

https://leetcode.com/problems/valid-parenthesis-string/
'''
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paranthesis, star = [], []
        for i in s:
            if i == '(' or i =='*':
                paranthesis.append(i)
            elif i == ')':
                if not paranthesis:
                    return False
                elif paranthesis[-1] != '(':
                    k = ''.join(paranthesis).rfind('(')
                    if k !=-1:
                        paranthesis.pop(k)
                    else:
                        paranthesis.pop()
                else:
                    paranthesis.pop()
        while '(' in paranthesis:
            n = paranthesis.index('(')
            if '*' in paranthesis[n+1:]:
                paranthesis = paranthesis[n+1:]
                paranthesis.pop(paranthesis.index('*'))
            else:
                return False
        return True
