'''
1332. Remove Palindromic Subsequences
Easy

Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.


Example 1:

Input: s = "ababa"
Output: 1
Explanation: String is already palindrome

https://leetcode.com/problems/remove-palindromic-subsequences/
'''
class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        elif s == s[::-1]:
            return 1
        return 2
