'''
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

https://leetcode.com/problems/palindrome-partitioning/
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.partitionRecu(result, [], s, 0)
        return result

    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur))
        else:
            for j in range(i, len(s)):
                #print i,j
                #print s[i:j+1]
                if self.isPalindrome(s[i: j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
