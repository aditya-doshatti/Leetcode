'''
409. Longest Palindrome
Easy

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

https://leetcode.com/problems/longest-palindrome/
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic, found, retVal = Counter(s), 0 , 0
        for key,val in dic.items():
            retVal += val
            if val%2:
                retVal -= 1
                found = 1
        return retVal+ found
