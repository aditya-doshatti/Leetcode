'''
821. Shortest Distance to a Character
Easy

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

https://leetcode.com/problems/shortest-distance-to-a-character/
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        retVal, prev = [], None
        curr = S.index(C)
        for i in range(len(S)):
            if S[i] == C:
                retVal.append(0)
                prev = curr
                if C in S[i+1:]:
                    curr = S[i+1:].index(C) + i+1
                else:
                    curr = None
            else:
                retVal.append(min(curr-i if curr is not None else float('inf'), 
                                 i-prev if prev is not None else float('inf')))
        return retVal
        # chars = []
        # for i in range(len(S)):
        #     if S[i] == C:
        #         chars.append(i)
        # retVal= []
        # for i in range(len(S)):
        #     k = min(abs(i - a) for a in chars)
        #     retVal.append(k)
        # return retVal
