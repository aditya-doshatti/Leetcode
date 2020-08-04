'''
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

https://leetcode.com/problems/valid-palindrome/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        retVal = True
        if s != "" and len(s) > 1:
            k = ''.join(ch for ch in s if ch.isalnum())
            n = len(k)
            if n > 0:
                if k[0].lower() == k[-1].lower():
                    for i in range(1,n//2):
                        if k[i].lower() == k[-(i+1)].lower():
                            pass
                        else:
                            retVal = False
                            break
                else:
                    retVal = False
        return retVal
