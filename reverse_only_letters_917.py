'''
917. Reverse Only Letters
Easy

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

https://leetcode.com/problems/reverse-only-letters/
'''
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)-1
        S = list(S)
        i = 0
        while i < n:
            if not S[i].isalpha():
                i += 1
                continue
            if not S[n].isalpha():
                n -= 1
                continue
            if S[i].isalpha() and S[n].isalpha():
                temp = S[i]
                S[i] = S[n]
                S[n] = temp
            i+=1
            n-=1
        return ''.join(S)
