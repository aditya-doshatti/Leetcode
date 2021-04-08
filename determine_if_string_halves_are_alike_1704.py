'''
1704. Determine if String Halves Are Alike
Easy

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

https://leetcode.com/problems/determine-if-string-halves-are-alike/
'''
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        mid = len(s)//2
        first = s[:mid]
        second = s[mid:]
        firstCnt, secondCnt = 0 ,0
        for val in vowels:
            if val in first:
                firstCnt += first.count(val)
            if val in second:
                secondCnt += second.count(val)
        return firstCnt == secondCnt
