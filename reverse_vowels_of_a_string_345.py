'''
345. Reverse Vowels of a String
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"

https://leetcode.com/problems/reverse-vowels-of-a-string/
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vov = {'a','A','e','E','i','I','o','O','u','U'}
        chars, idx = [], []
        for i, char in enumerate(s):
            if char in vov:
                chars.append(char)
                idx.append(i)
        idx.reverse()
        s =list(s)
        for i in range(len(chars)):
            s[idx[i]] = chars[i]
        return ''.join(s)
