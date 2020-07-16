'''
151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

https://leetcode.com/problems/reverse-words-in-a-string/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
